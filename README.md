# py2048
2048 game

**On Windows**:
<br />
	This code makes use of msvcrt module of python to implement getch type function. This feature is available only for Windows/DOS.

**For UNIX based operating system**:
<br />
 1)First install pip3 or pip depending upon python version. To check python version, type _```python --version ```_  . You should see something like this.
 <br />
 ![test-python](https://user-images.githubusercontent.com/64476047/82217543-3256f780-9938-11ea-9fa1-270a0a452898.png)
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
 ![initial setup](https://user-images.githubusercontent.com/64476047/82215205-a42d4200-9934-11ea-954f-e25c320d758a.png)
 <br />
 In this example board size is 3 and number required to win is 32.
<br />
 2)Press ```w/a/s/d to shift numbers up/left/down/right respectively and e to quit.```
 <br />
 3)If you enter any invalid move, i.e board doesn't change with a particular move played, it will ask you to try another move. 
 <br /> 
 In the previous example, if we play "w" board doesn't change.
 <br />
 ![invalid move](https://user-images.githubusercontent.com/64476047/82216909-40584880-9937-11ea-8910-16c2ba6ef5dc.png)
<br />
 4)On entering any valid move, the board will change accordingly. This is an intermediate stage of same example.
 <br />
 ![intermediate final](https://user-images.githubusercontent.com/64476047/82215738-7bf21300-9935-11ea-9fcc-4ed0f990ece7.png)
 <br />
 5)When you get the required number to win(X) on your board, you win the game and the program stops. In this example, since we got the highlighted number(32), program gives a message game won
 <br />
 ![game won final](https://user-images.githubusercontent.com/64476047/82216234-4bf73f80-9936-11ea-98e2-077044623a05.png)
<br />
 6)Other case, if you can’t play any more moves, you get a message game lost and program stops. It looks like this.                
 ![game lost final](https://user-images.githubusercontent.com/64476047/82214962-3c76f700-9934-11ea-9a90-2a7b0cb6ff55.png)




                                                                                        -Done by Kalyani Sains.
