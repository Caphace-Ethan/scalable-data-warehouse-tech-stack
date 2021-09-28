import math
import pandas as pd
import contextlib
import os
import subprocess
data_path = './data/I80_davis.txt'
csv_path = './data/batch_'
csv_path1 = './dbt/data/sensors_data.csv'
txt_path = "./data/batch_"
_new_file = './data/batch'


def split_text():
	l = 3 * 10 ** 6  # lines per split file
	with contextlib.ExitStack() as stack:
		try:
			fd_in = stack.enter_context(open(data_path))
			for i, line in enumerate(fd_in):
				print(f" Progress: {round((i*100)/l,2)} %")
				if not i % l:
					file_split = '{}_{}.txt'.format(_new_file, i // l)
					fd_out = stack.enter_context(open(file_split, 'w'))
				fd_out.write('{}\n'.format(line))
			loggs = "Reading large txt file successfully,  Splitting file to small files successfully"
		except Exception as e:
			loggs = "Read txt file Un-successfully, error: "+ e

	return loggs


def _get_text_corpus_to_csv():
	for ii in range(12):
		csv_file = pd.read_csv(txt_path+str(ii)+".txt", header=None)
		csv_file.columns = ['utc_time_id', 'source_id', 'source_ref',
							'avg_freeflow_speed', 'avg_travel_time',
							'high_quality_samples', 'samples_below_100pct_ff',
							'samples_below_95pct_ff', 'samples_below_90pct_ff',
							'samples_below_85pct_ff', 'samples_below_80pct_ff',
							'samples_below_75pct_ff', 'samples_below_70pct_ff',
							'samples_below_65pct_ff', 'samples_below_60pct_ff',
							'samples_below_55pct_ff', 'samples_below_50pct_ff',
							'samples_below_45pct_ff', 'samples_below_40pct_ff',
							'samples_below_35pct_ff', 'samples_below_30pct_ff',
							'samples_below_25pct_ff', 'samples_below_20pct_ff',
							'samples_below_15pct_ff', 'samples_below_10pct_ff',
							'samples_below_5pct_ff'
							]

		print(f" Progress: {round((ii * 100) / 12, 2)} % ...")
		try:
			csv_file.to_csv(csv_path + str(ii) + '.csv', index=False)
			e = "CSV Created"
		except Exception as e:
			print(e)
		print(e)

	# sed	1d batch_ *.csv > ../dbt/data/all_sensor_data.csv

	return e


if __name__ == "__main__":
	#  For Testing purposes
	if (False):
		returned_ = _get_text_corpus_to_csv()
		print(returned_)

	elif (False):
		split_text()

	elif (False):
		home_dir = os.system("cd ..")
		print(home_dir)
		os.system("./split_txt_file.sh")



