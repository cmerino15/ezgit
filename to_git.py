import pyautogui

# pause for one sec after each pyautogui command
pyautogui.PAUSE = 1

# minimize python program ... in order to get to working directory
pyautogui.hotkey('win', 'down')

# current directory search bar
pyautogui.keyDown('alt')
pyautogui.press('d')
pyautogui.keyUp('alt')

# opens terminal in current working directory
pyautogui.write('cmd')
pyautogui.press('enter')

# venv, requirements
pyautogui.write('py -m venv env')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.write(r'env\scripts\activate') # bug where \a is not showing
pyautogui.press('enter')

# .gitignore
pyautogui.write('echo env/ > .gitignore')
pyautogui.press('enter')
pyautogui.write('echo to_git.py >> .gitignore')
pyautogui.press('enter')

# readme
pyautogui.write('echo install the python packages using pip install module_name > readme.md')
pyautogui.press('enter')
pyautogui.write('echo remember to run pip freeze ^> requirements.txt when ready >> readme.md')
pyautogui.press('enter')
pyautogui.write('echo finally remember to deactivate the venv on each activation >> readme.md')
pyautogui.press('enter')

# images folder
pyautogui.write('mkdir images')
pyautogui.press('enter')

# git init
pyautogui.write('git init')
pyautogui.press('enter')
pyautogui.write('git add -A')
pyautogui.press('enter')
pyautogui.write('git commit -m "first commit"')
pyautogui.press('enter')
pyautogui.write('git branch -M main')
pyautogui.press('enter')
uname = pyautogui.prompt(text='', title='github username', default='')
rname = pyautogui.prompt(text='', title='name of repo', default='')
pyautogui.write('git remote add origin git@github.com:{}/{}.git'.format(uname, rname))
pyautogui.press('enter')
pyautogui.write('git push origin main')
pyautogui.press('enter')

# deactivate venv
pyautogui.write('deactivate')
pyautogui.press('enter')



