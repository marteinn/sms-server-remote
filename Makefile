# Absolute path to project
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

update_dependencies:
	cd src/incoming_sms && pip install -t vendored/ -r requirements.txt
	rm -r $(ROOT_DIR)/src/incoming_sms/vendored/Crypto || true
	rm -r $(ROOT_DIR)/src/incoming_sms/vendored/pycrypto-2.6.1.dist-info || true
	wget -O "/tmp/awslambda-pycrypto.zip" "https://github.com/Doerge/awslambda-pycrypto/archive/master.zip"
	unzip /tmp/awslambda-pycrypto.zip -d /tmp/
	mv /tmp/awslambda-pycrypto-master/Crypto $(ROOT_DIR)/src/incoming_sms/vendored
	mv /tmp/awslambda-pycrypto-master/pycrypto-2.6.1.dist-info $(ROOT_DIR)/src/incoming_sms/vendored
	rm /tmp/awslambda-pycrypto.zip || true
	rm -rf /tmp/awslambda-pycrypto-master || true
