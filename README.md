[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8843626&assignment_repo_type=AssignmentRepo)
# Minecraft Scure API
This is the README file for Assignment 3 in Programming Studio 2 (COSC2804).

If you would like to test the extension of Raspberry Juice and MCPI yourself, follow these steps:

1- navigate to RaspberryJuice -> src -> main -> java -> RemoteSession.java

2- in this file you must locate all instances of file path, they are located on the following lines: 1044,1070, 1075, 1090, 1094. Change these lines to contain  the local path of the pem files. 

3- install maven.

4- open your terminal and navigate to the RaspberryJuice directory

5- use Maven to compile a jar file (in windows use cmd to navigate the the directory then type "mvn package")

6 - locate the created jar file (usually in target folder) and copy it.

7 - Navigate to your minecraft server folder -> plugins

8 - replace the raspberryjuice-1.12.1.jar file with the copied file.

9 - run the server

10 - navigate to SymmetricKey.py and run the code (you will only need to do this once)

11- finally, you can use main.py to securely send messages from MCPI client to the Java server (by default its sends message directly to server using port 4711)



Please indicate where to find your video demo. You can include it in this repo if it's small enough, or alternatively use a video sharing platform, such as YouTube. Any widely supported video format is fine (.mp4, .avi, .mkv, etc.)

# Mandatory: Student contributions
Please summarise each team member's contributions here. Include both an approximate, percentage-based breakdown (e.g., "Anna: 25%, Tom: 25%, Claire: 25%, Halil: 25%") **and a high-level summary of what each member worked on, in dot-point form**.
Zenabden 25%:
- Assisted with extending Raspberry Juice and MCPI
- Demonstrated security weakness of the original MCPI
- assisted with research and completion of reports
- Created video demonstration and explanation of code.
- assisted in all areas

Duc 25%: 
- Extended Raspberry Juice and MCPI
- Assisted with video demonstration
- Researched different Encryption methods and decided on Encrypt then Mac
- Assisted with Report 2-1.
- assisted in all areas


Matt 25%:
- Assisted in organising methodology and implementing RSA method
- helped extend raspberry juice and mcpi
- Did Report 2-2
- Assisted with Report 2-1.
- assisted in all areas

Sandrup 25%:
- Compelted Report 2-2
- did intensive research to identify references for report
- Did phase 1 report
- identifyed security weakness of original MCPI.
- assisted in all areas

