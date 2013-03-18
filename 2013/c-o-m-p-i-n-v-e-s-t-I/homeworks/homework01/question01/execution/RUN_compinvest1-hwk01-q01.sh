
 getDataScript=../code/get-data.py
myPythonScript=../code/compinvest1-hwk01-q01.py
      code_dir=../code
    output_dir=../output
       tmp_dir=${output_dir}/tmp

##################################################
if [ ! -d ${output_dir} ]; then
	mkdir ${output_dir}
fi

if [ ! -d ${tmp_dir} ]; then
	mkdir ${tmp_dir}
fi

cd ${output_dir}

#stdoutFile=stdout.py.`basename ${getDataScript} .py`
#python ${getDataScript} 2>&1 > ${stdoutFile}

stdoutFile=stdout.py.`basename ${myPythonScript} .py`
python ${myPythonScript} 2>&1 > ${stdoutFile}

##################################################
#python ${output_dir} ${code_dir} ${tmp_dir} < ${myRscript} 2>&1 > ${stdoutFile}

