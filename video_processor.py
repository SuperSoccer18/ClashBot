import os
import cv2
from PIL import Image
from utils import display_img, pil_to_cv2

class VideoProcessor:
    def __init__(self, video_path, target_fps=2.0, start=0.0, end=None):
        self.video_path = video_path
        self.target_fps = float(target_fps) if target_fps else 2.0
        self.start = max(0.0, float(start or 0.0))
        self.end = float(end) if end is not None else None
        self.cap = None
        self.video_fps = 0.0

    def load(self):
        if self.cap is not None:
            return
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video: {self.video_path}")
        if self.start > 0:
            cap.set(cv2.CAP_PROP_POS_MSEC, self.start * 1000.0)
        fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
        self.video_fps = fps if fps and fps > 0 else 0.0
        self.cap = cap

    def close(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def frames(self):
        """
        Iterate over frames as PIL.Image at the configured extraction rate.
        """
        self.load()
        interval = 1.0 / max(1e-9, self.target_fps)
        next_t = float(self.start)
        idx = 0
        try:
            while True:
                ok, frame = self.cap.read()
                if not ok or frame is None:
                    break

                t_ms = self.cap.get(cv2.CAP_PROP_POS_MSEC)
                if t_ms is not None and t_ms >= 0:
                    t = t_ms / 1000.0
                elif self.video_fps > 0:
                    t = idx / self.video_fps
                else:
                    t = idx / 30.0  # fallback

                if self.end is not None and t > self.end:
                    break

                if t + 1e-6 >= next_t:
                    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    yield Image.fromarray(rgb)
                    next_t += interval

                idx += 1
        finally:
            self.close()

    def extract(self):
        """
        Return a list of PIL.Image frames for downstream analysis.
        """
        return list(self.frames())

    def save_frames(self, save_dir, prefix="frame", ext="png"):
        """
        Save extracted frames to disk; returns the count saved.
        """
        os.makedirs(save_dir, exist_ok=True)
        count = 0
        for img in self.frames():
            img.save(os.path.join(save_dir, f"{prefix}_{count:06d}.{ext}"))
            count += 1
        return count

# Testing
# def show_images(images):
#     for image in images:
#         image = pil_to_cv2(image)
#         display_img(image)

# video_path = 'data/2.6Hog_720p_[zfg4k8xy6JQ].mp4'
# videoprocessor = VideoProcessor(video_path, target_fps=2.0, start=0.0, end=50.0)
# frames = videoprocessor.frames()
# show_images(frames)