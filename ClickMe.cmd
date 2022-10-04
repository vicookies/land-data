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
    echo "没有找到msedgedriver.exe"
    if exist "msedgedriver.tar.gz" (
        powershell tar -zxvf msedgedriver.tar.gz
        if exist "msedgedriver.exe" (
             python ./worm.py
        ) 
    ) else (    
        echo "没有找到msedgedriver.tar.gz"
        echo "正在下载webdriver到本文件目录下"
        start https://msedgedriver.azureedge.net/105.0.1343.53/edgedriver_win64.zip
        echo "下载后请解压至当前目录,并重新执行本文件"
    )

)
pause
exit

:pythonnoexist 
echo "没有找到python,请安装python,并重新执行本文件"  
start https://apps.microsoft.com/store/detail/python-39/9P7QFQMJRFP7?hl=zh-cn&gl=CN
pause
exit