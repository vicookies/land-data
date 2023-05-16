python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple

if exist "msedgedriver.exe" (
    python ./worm.py
) else (
    echo "û���ҵ�msedgedriver.tar.gz"
    echo "��������Ӧwebdriver�����ļ�Ŀ¼��"
    start https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    echo "���غ����ѹ����ǰĿ¼,������ִ�б��ļ�"
)
pause
exit
