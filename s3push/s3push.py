
def s3_upload(filename):
	import tinys3
	import yaml

	with open("config.yml", 'r') as ymlfile:
		config = yaml.load(ymlfile)

	s3 = tinys3.Connection(config['s3']['access_key_id'], config['s3']['secret_access_key'])
	file_handle = open(filename, 'rb')
	s3.upload(filename, file_handle, config['s3']['bucket_name'],headers={'x-amz-meta-cache-control': 'max-age=60'})

