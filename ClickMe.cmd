@echo off
set flag=0
@for /f "tokens=2" %%h in ('python -h ^| findstr /C:"usage:"') do ^
set PYVER2=%%h
@if "%PYVER2%" == "python" (@set flag=1)
if %flag% == 1 goto pythonexist

:pythonexist 
python -m pip install --upgrade pip   
pip install selenium
pip install msedge-selenium-tools
if exist "msedgedriver.exe" (
    python ./worm.py
) else (
    echo "û���ҵ�msedgedriver.exe"
    echo "�������������edge://version/�鿴edge�汾,������Ӧ��webdriver�����ļ�Ŀ¼��,������ִ�б��ļ�"
    start https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
)
pause
exit

:pythonnoexist 
echo "û���ҵ�python,�밲װpython,������ִ�б��ļ�"  
start https://apps.microsoft.com/store/detail/python-39/9P7QFQMJRFP7?hl=zh-cn&gl=CN
pause
exit