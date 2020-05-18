# py2048
2048 game

**On Windows**:
<br />
	This code makes use of msvcrt module of python to implement getch type function. This feature is available only for Windows/DOS.

**For UNIX based operating system**:
<br />
 1)First install pip3 or pip depending upon python version. To check python version, type _```python --version ```_  .
 <br />
 2)Then type _```sudo apt-get install pip3```_ or _```sudo apt-get install pip_```. 
 <br />
 3)For downloading getch function, _```pip3 install getch```_. You can now run the code.
 <br />
 4)Other modules used in this code are “os”, “argparse”, “random”, “copy”, “math". If not available, they can be installed in similar manner.

**How to run**:
<br />
 1)For windows, open command prompt or Windows Powershell and type _```python filename --n N --x X```_, where N and X are board size and number required to win respectively and filename has “.py” extension. If you don’t want to specify any input, just write _```python filename```_;
or to specify any one input, just write that respective argument only, else you’ll get error.   Whenever not specified, default will set N to 5 and X to 2048. Ensure that X is a power of two; else you’ll never win.
 <br />
 2)For Unix based, type _```python3 filename --n N --x X```_,  or python2 depending upon python version. Rest is similar to windows.
<br />

**How it works** : 
<br />
 1)After you run the program, it will display the board of specified dimensions.
 <br />
 2)Press ```w/a/s/d to shift numbers up/left/down/right respectively and e to quit.```
 <br />
 3)If you enter any invalid move, i.e board doesn't change with a particular move played, it will ask you to try another move.  
 4)On entering any valid move, the board will change accordingly. 
 <br />
 5)When you get the required number to win(X) on your board, you win the game and the program stops.
 <br />
 6)Other case, if you can’t play any more moves, you get a message game lost and program stops.                
 


                                                                                        -Done by Kalyani Sains.
