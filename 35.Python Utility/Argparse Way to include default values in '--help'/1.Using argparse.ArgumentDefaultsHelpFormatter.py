import argparse
parser = argparse.ArgumentParser(description="GeeksforGeeks argparse Example1",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--course', type=str, default='Python', help='Course name at GeeksforGeeks')
parser.add_argument('--duration', type=int, default=10, help='Course duration in weeks')
parser.add_argument('--level', type=str, default='Beginner', help='Course difficulty level')
args = parser.parse_args()
print(f"Course: {args.course}")
print(f"Duration: {args.duration} weeks")
print(f"Level: {args.level}")
