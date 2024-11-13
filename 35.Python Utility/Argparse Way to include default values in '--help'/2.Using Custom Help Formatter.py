import argparse
class CustomHelpFormatter(argparse.HelpFormatter):
    def _get_help_string(self, action):
        help = action.help
        if action.default is not argparse.SUPPRESS:
            help += f' (default: {action.default})'
        return help
parser = argparse.ArgumentParser(description="GeeksforGeeks argparse Example 2",
                                 formatter_class=CustomHelpFormatter)
parser.add_argument('--course', type=str, default='Python', help='Course name at GeeksforGeeks')
parser.add_argument('--duration', type=int, default=10, help='Course duration in weeks')
parser.add_argument('--level', type=str, default='Beginner', help='Course difficulty level')
args = parser.parse_args()
print(f"Course: {args.course}")
print(f"Duration: {args.duration} weeks")
print(f"Level: {args.level}")
