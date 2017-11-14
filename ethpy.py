#!/usr/bin/python

from ethereum import utils
import os

count = 0
while count < 50:
	private_key = utils.sha3(os.urandom(4096))
	raw_address = utils.privtoaddr(private_key)
	account_address = utils.checksum_encode(raw_address)
	priv = utils.encode_hex(private_key)

	print account_address, priv
	count += 1
