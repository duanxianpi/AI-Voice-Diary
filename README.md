# AI-Voice-Diary
## Installation

```bash
pip install -r requirements.txt
```

### PyAudio
On Windows PyAudio may failed to install please check [here](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14)

## Usage
```bash
python mainwindow.py
```

## Inspiration
At the beginning of a new year, I always want to look back at the past year. However, each time I can't find much of a record of the past year. Even though I have a diary but I don't actually write down a few serious diary entries during the year. 

I think the reason for this is that I think journaling is a time-consuming and laborious task, so I decided to take this opportunity to develop a software to help you keep a journal.

## What it does
Unlike other traditional diary software, AI Voice Diary uses voice recording instead of writing or typing, which is more convenient and easiler to use. It is always easier to speak than to write. 

### Selecting you mood
![image.png](https://s2.loli.net/2022/01/23/FROPn2LVtqySUdp.png)

You can choose you feeling tody. It will help you quickly recall what happened today before you start recording.

### AI Transcript
With the help of AssemblyAI,  AI Voice Diary can help you transcript your recording, you don't need to type it by yourself. It is all automatically!

 ### Key Words extract
#### You don't know what you should talk? No Worries!!!
The AI will help you extract the key words in your record. You just need to talk whatever you wanted to talk.

## How we built it
Initially, I wanted to make it into a mobile app but I had no relevant development experience and I gave up after trying for a while. The reason why I chose Python and PySide is that Python has well support HTTP library can greatly reduce the workload. What's more I had some experience in C++ and Qt.

The GUI part is built with Qt and the sound part is based on PyAudio. Finally the AI part is based on AssemblyAI.

## Challenges we ran into
Even though I have experience with Qt development, it was still a challenge to connect Python with Qt by PySide. Many functions are a bit different to use, such as the use of ui files and the connection between signals and slots.

Another challenge is the UI. Designing a beautiful UI for me is a daunting task. I've try my best to make the software less boring. However, it still doesn't look attractive enough.

## Accomplishments that we're proud of
This was my first hackathon and I didn't even think I would successfully complete a project before the hackathon. So for me, successfully completing this challenge is already a big achievement and it makes me very proud.

## What we learned
I learned how to use Pyside to create gui programs also learned to use AssemblyAI for speech recognition. I have also gained a better understanding of Hackathon.

## What's next for AI Voice Diary
Continue to improve new features such as the progress bar and design a more attractive UI.
 If I have the chance, I will bring it to mobile platforms such as Android and IOS. If someone is interested to work with me you are welcome to contact me.
