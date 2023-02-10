pw=`dirname $0`
export PATH=$pw:$PATH
export OPENSSL_CONF=$pw/openssl.cnf
python3 $pw/main.py
today=$(date)
echo "-------" $today " End of Process-------"

