import math
import hashlib
import base64
import string

print('''

 ██▓███ ▓██   ██▓▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██░  ██▒▒██  ██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▓██░ ██▓▒ ▒██ ██░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▒██▄█▓▒ ▒ ░ ▐██▓░░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██▒ ░  ░ ░ ██▒▓░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒▓▒░ ░  ░  ██▒▒▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░▒ ░     ▓██ ░▒░     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░░       ▒ ▒ ░░    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
         ░ ░                  ░ ░      ░ ░      ░  ░      ░  
         ░ ░                                                 

''')	
print("                                                       .... coded by shivraj patil")

while True:

	print('\n')
	print("enter enceyption method: ")
	print("1. reverse cypher ")
	print("2. ceser cypher ")
	print("3. Transposition cypher")
	print("4. Vernam Cypher")
	print("5. md5 encoding")
	print("6. base64 encoding")
	print("7. XOR cypher")
	print("8. Affine cypher")
	print("9. vegnare cypher")
	print("10. Substitution cypher")
	print('\n')
	no = input("Enter no: ")

	if no == '1':
		text = input("enter msg to Encrypt: ")

		translated = '' 
		i = len(text) - 1

		while i >= 0:
		   translated = translated + text[i]
		   i = i - 1
		print("The cipher text in reverse cypher is : ", translated)

	if no == '2':
		text = input("enter msg to Encrypt: ")
		shi = input("enter shift for ceser cypher: ")
		s = int(shi)
		def encrypt(text,s):
			result = ""

			# traverse text
			for i in range(len(text)):
				char = text[i]

				# Encrypt uppercase characters
				if (char.isupper()):
					result += chr((ord(char) + s-65) % 26 + 65)

				# Encrypt lowercase characters
				else:
					result += chr((ord(char) + s - 97) % 26 + 97)

			return result

		print ("Text : " + text)
		print ("Shift : " + str(s))
		print ("text in ceser cypher: " + encrypt(text,s))

	if no == '3':
		def encryptMessage(msg):
			cipher = ""

			# track key indices
			k_indx = 0

			msg_len = float(len(msg))
			msg_lst = list(msg)
			key_lst = sorted(list(key))

			# calculate column of the matrix
			col = len(key)
			
			# calculate maximum row of the matrix
			row = int(math.ceil(msg_len / col))

			# add the padding character '_' in empty
			# the empty cell of the matix
			fill_null = int((row * col) - msg_len)
			msg_lst.extend('_' * fill_null)

			# create Matrix and insert message and
			# padding characters row-wise
			matrix = [msg_lst[i: i + col]
					for i in range(0, len(msg_lst), col)]

			# read matrix column-wise using key
			for _ in range(col):
				curr_idx = key.index(key_lst[k_indx])
				cipher += ''.join([row[curr_idx]
								for row in matrix])
				k_indx += 1

			return cipher


		msg = input("enter msg for columner transposition: ")
		print("NOTE: key doesn't contain repeting letters: ")
		key = input("Enter key: ")


		cipher = encryptMessage(msg)
		print("Encrypted Message: {}".
					format(cipher))
	if no == '4':
		def makeVernamCypher( text, key ):
		    answer = "" 
		    p = 0 
		    for char in text:
		        answer += chr(ord(char) ^ ord(key[p]))
		        p += 1
		        if p==len(key):
		            p = 0
		    return answer
		MY_KEY = "cvwopslweinedvq9fnasdlkfn2"
		
		print("\n\n---Vernam Cypher---")
		PlainText = input("Enter text to encrypt: ")
		    
		Cypher = makeVernamCypher(PlainText, MY_KEY)
		print("Cypher text: "+Cypher)

	if no == '5':
		str = input("Enter your msg to encrypt: ")

		result = hashlib.sha256(str.encode())

		print("The hexadecimal equivalent of SHA256 is : ")
		print(result.hexdigest())

		print ("\r")

		result = hashlib.sha384(str.encode())

		print("The hexadecimal equivalent of SHA384 is : ")
		print(result.hexdigest())

		print ("\r")

		result = hashlib.sha224(str.encode())

		# printing the equivalent hexadecimal value.
		print("The hexadecimal equivalent of SHA224 is : ")
		print(result.hexdigest())

		print ("\r")


		result = hashlib.sha512(str.encode())

		
		print("The hexadecimal equivalent of SHA512 is : ")
		print(result.hexdigest())

		print ("\r")

		
		result = hashlib.sha1(str.encode())

		print("The hexadecimal equivalent of SHA1 is : ")
		print(result.hexdigest())

	if no == '6':
		sample_string = input("enter msg to encrypt: ")
		sample_string_bytes = sample_string.encode("ascii")

		base64_bytes = base64.b64encode(sample_string_bytes)
		base64_string = base64_bytes.decode("ascii")

		print(f"Encoded string: {base64_string}")


	if no == '7':
		def encryptDecrypt(inpString):
		    xorKey = 'P'
		    
		    length = len(inpString)

		    for i in range(length):
		    
		        inpString = (inpString[:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i + 1:])
		        print(inpString[i], end = "")
		    
		    return inpString;

		sampleString = input("enter your msg : ")
	    
		print("Encrypted String: ", end = "")
		sampleString = encryptDecrypt(sampleString)

	if no == '8':

		def egcd(a, b):
		    x,y, u,v = 0,1, 1,0
		    while a != 0:
		        q, r = b//a, b%a
		        m, n = x-u*q, y-v*q
		        b,a, x,y, u,v = a,r, u,v, m,n
		    gcd = b
		    return gcd, x, y

		def modinv(a, m):
		    gcd, x, y = egcd(a, m)
		    if gcd != 1:
		        return None 
		    else:
		        return x % m


		def affine_encrypt(text, key):
		    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
		                + ord('A')) for t in text.upper().replace(' ', '') ])

	    
		text = input("enter msg: ")
		key = [17, 20]

		   
		affine_encrypted_text = affine_encrypt(text, key)

		print('Encrypted Text: {}'.format( affine_encrypted_text ))


	if no == '9':
		def solve(text, key):
		    cip = []
		    start = ord('a')
		    for l, k in zip(text, key):
		         shift = ord(k) - start
		         pos = start + (ord(l) - start + shift) % 26
		         cip.append(chr(pos))
		    return ''.join([l for l in cip])

		text = input(" enter your msg: ")
		key = input("enter key: ")
		print("encrypted text : ")
		print(solve(text, key))

	if no == '10':
		all_letters= string.ascii_letters



		    
		dict1 = {}
		key = 4

		for i in range(len(all_letters)):
		    dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]


		plain_txt= input("enter msg to encrypt: ")
		cipher_txt=[]


		for char in plain_txt:
		    if char in all_letters:
		        temp = dict1[char]
		        cipher_txt.append(temp)
		    else:
		        temp =char
		        cipher_txt.append(temp)
		        
		cipher_txt= "".join(cipher_txt)
		print("Cipher Text is: ",cipher_txt)

		    
		dict2 = {}  
		for i in range(len(all_letters)):
		    dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
		    
		# loop to recover plain text
		decrypt_txt = []

		for char in cipher_txt:
		    if char in all_letters:
		        temp = dict2[char]
		        decrypt_txt.append(temp)
		    else:
		        temp = char
		        decrypt_txt.append(temp)
		        
		decrypt_txt = "".join(decrypt_txt)
		print("Recovered plain text :", decrypt_txt)
