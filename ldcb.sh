python rfc_module_enable.py $1 $2 
sleep 1
python load_codebook.py $1 0 $2 
python load_codebook.py $1 1 $2 
