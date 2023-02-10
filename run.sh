pw=`dirname $0`
export PATH=$pw:$PATH
echo $PATH
export OPENSSL_CONF=$pw/openssl.cnf
python3 $pw/main.py 
