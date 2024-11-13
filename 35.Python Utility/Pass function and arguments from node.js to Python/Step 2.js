import {spawn} from "child_process";

let argument = "True";
const pythonProcess = spawn('python3', ['-c',
`import compliment; compliment.giveMe(${argument});`]);
pythonProcess.stdout.on('data', (data) => {
	console.log(`stdout: ${data}`);
});
pythonProcess.stderr.on('data', (data) => {
	console.log(`stderr: ${data}`);
});
pythonProcess.on('exit', (code) => {
	console.log(`Python process ended with code: ${code}`);
});
