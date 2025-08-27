import video_processor
from detectors.main_detector import MainDetector
import utils
import cv2

class VideoLabeler:
    def __init__(self, main_detector, video_path, target_fps=2.0, start=5, end=None):
        self.video_processor = video_processor.VideoProcessor(video_path, target_fps, start, end)
        self.main_detector = main_detector

    def label(self):
        frames = self.video_processor.frames()
        for frame in frames:
            cv_img = utils.pil_to_cv2(frame)
            cv2.imshow("Video Frame", cv_img)

            results = self.main_detector.run(frame)
            print('Cards:', results['cards'])
            print('Numbers:', results['numbers'])
            print('Units:', results['units'])

            cv2.waitKey(0)  # wait for any key
            cv2.destroyWindow("Video Frame")


# Testing
md = MainDetector()
vid_labeler = VideoLabeler(md, 'data/2.6Hog_720p_[zfg4k8xy6JQ].mp4', target_fps=2.0, start=0.0, end=10.0)
vid_labeler.label()