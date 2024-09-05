import cv2

# https://docs.opencv.org/4.x/

def run() -> None:
	video_cap = cv2.VideoCapture(0)

	while(True):
		frame = video_cap.read()

		cv2.imshow("Your face", frame)

		if(cv2.waitKey(1) == ord('q')):
			print("Exiting...")
			break

def main() -> int:
	print("Identifying Face...")

	run()

if(__name__ == "__main__"):
	main()
