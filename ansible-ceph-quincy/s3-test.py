import boto
import boto.s3.connection

access_key = '72HWGAIHEJENTA7MCSRX'
secret_key = 'UpQEaWARyKIVM4suQbgpSnCgDykoch83mm4yKsQT'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'ceph1', port = 7480,
        is_secure=False, calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
bucket = conn.create_bucket('bit-bucket')
    for bucket in conn.get_all_buckets():
            print "{name}".format(
                    name = bucket.name,
                    created = bucket.creation_date,
 )
