echo " Build Start"

python3.9 -m pip install django
python3.9 manage.py collectstatic --noinput --clear

echo " Build Stop"