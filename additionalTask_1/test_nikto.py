import subprocess
import pytest

@pytest.mark.nikto
def test_nikto_output():
    # Выполнение команды nikto
    command = "nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Проверка наличия текста "0 error(s)" в выводе команды
    assert "0 error(s)" in result.stdout, f"Expected '0 error(s)' not found in output:\n{result.stdout}"

    # Вывод результатов команды
    print("Nikto command output:")
    print(result.stdout)
