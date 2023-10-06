# Audio-to-Sign-language-Translator
KLE Dr. M. S. SHESHGIRI COLLEGE OF ENGINEERING AND TECHNOLOGY
UDYAMBAG, BELAGAVI - 590008
(CONSTITUENT COLLEGE OF KLE TECHNOLOGICAL UNIVERSITY,HUBBALLI,BELAGAVI CAMPUS)
Ph.No.(0831)-2440322    Fax No.: (0831)-2441644 	Email: principal@klescet.in Web: www.klescet.ac.in

Department of Computer Science and Engineering

Project Work Phase - 1 (18CSP77)

Synopsis on
“AUDIO TO SIGN LANGUAGE TRANSLATION”

Under the Guidance of
Prof. Roopa Patil
Dept. of CSE, KLE Dr. MSSCET, Belagavi.

Submission by
                                           Ms. Gouri Dumale   		   USN:2KL18CS021
                                           Ms. Kanade Harshada Ashok     USN:2KL18CS026
                                           Ms. Sandhya D Kumbhar	   USN:2KL18CS077


Recommendations	Remarks
Guide Approval	Yes/ No	
Review Committee Approval	Yes/ No	

HOD Approval	Yes/ No	

Academic Year 2021-22
Introduction
	India, a nation with a populace of 1.3 billion individuals, almost a fifth of the total populace [7], is evaluated to have individuals with hearing loss of the request for 5 million [8]. As per the Government of India Disabled Persons Statistics Survey 2016 [35], 32.5% of this number is comprised of kids. In the review, for the age-bunch 5–9 years of age, 209 of an example set of 100,000 kids and for the age group of 10–14 years of age, 212 of a lot of 100,000 youngsters have been discovered hearing impeded. A critical segment of this populace, to be specific 32% of these youngsters have a significant hearing misfortune, and 39% are determined to have serious hearing misfortune.
	To communicate with each other and with other deaf people, deaf people require sign language. It is important for a deaf person's psychological, mental, and linguistic advancement to have access to a sign language.

Problem Statement
u	Sign language recognition system, which would convert audio to Sign language. This must be a good application for the deaf and the non-deaf people who wants to communicate with each other.

Objectives
1.	To implement deep learning algorithm : Mel – frequency Cepstral Coefficient(MFCC).
2.	To implement porter stemming algorithm, subject-object-verb rule based syntax module.

Methodology
Step 1: The inputs can be of forms: 
• Live speech input
• Recorded audio file input
Step 2 : The live speech is received as input from the microphone of our system. This is done using the Python package PyAudio. PyAudio is a Python package that is used to record audio on a variety of platforms. The audio thus received is converted into text using NLP techniques.

Step 3 : Extracting feature form speech is an important stage in our method. The procedures used for extracting feature form speech is MelFrequency Cepstral Coefficients (MFCCs). The algorithm starts with preprocessing and signal conditioning. Next extracting feature form speech using Cepstral coefficients will be done. Then the result of this process sends to segmentation part. Finally recognition part recognizes the words.
Step 4 : Pre-processing of text - The filler words which are used to fill the gap in the sentence are apparently lesser-meaning words.They provide less context to the sentence. There are around 30+ filler words in the English Language which hardly makes sense in the sentence. So, the system removes the filler words from the sentence and makes it more meaningful. By removing these words, the system will save time.The system also removes any punctuations present in the sentence and makes the sentence only contain alphabets and numbers.
Step 5 : Porter Stemming Algorithm - Porter Stemming algorithm provides a basic approach to conflation that may work well in practice. Natural Language Processing (NLP) helps the computer to understand the human natural language. Porter Stemming is one of the Natural Language Processing techniques. Porter Stemmer algorithm is known for its speed and ease. It is mainly used for data mining and to retrieve information. It produces better results than any other stemming algorithms. It has less error rate.
Step 6 : The system iterates through every word in the processed text sentence which is received from the previous step and searches the corresponding sign language video sequences in the local system. If the word is found, the system shows the output as a video sequence using the OpenCV module in Python.If the word is not found in the local system, the system will search for the word in a sign language repository named “Indian Sign Language Portal”. The system looks for the video link in the Indian Sign Language Portal by webscraping. And plays the corresponding sign language video sequence.  










Block Diagram

           LIVE SPEECH/RECORDED SPEECH











Hardware & Software Requirements
Hardware Requirements:
•	System with microphone.
Software Requirements:
•	Python Libraries
•	NLP modules

Expected Outcomes
Audio to sign language translation system does live conversion of input audio to Indian Sign Language (ISL) in the form of images or videos. It reduces the communication gap between deaf and non-deaf people.


References
[1]	Reference 1 : Ankita Harkude, Sarika Namade, Shefali Patil, Anita Morey “Audio to Sign Language Translation for Deaf People” ISSN: 2277-3754, International Journal of Engineering and Innovative Technology (IJEIT) Volume 9, Issue 10, April 2020.
[2]	Reference 2 : Ezhumalai P , Raj Kumar M, Rahul A S, Vimalanathan V, Yuvaraj  A “Speech To Sign Language Translator For Hearing Impaired” Turkish Journal of Computer and Mathematics Education
[3]	Reference 3 : Khalid Khalil El-Darymli1 , Othman O. Khalifa1 and Hassan Enemosah1  “Speech to Sign Language Interpreter System (SSLIS)”
[4]	Reference 4 : Prof. Abhishek Mehta, Dr. Kamini Solanki , Prof. Trupti Rathod “Automatic Translate Real-Time Voice to Sign Language Conversion for Deaf and Dumb People”, International Journal of Engineering Research & Technology (IJERT) ISSN: 2278-0181
  
The proposed project synopsis is approved by guide and forwarded for kind consideration. 
Batch No.	Student Name with Signature	USN	Guide Name	Signature

	Gouri Dumale	2KL18CS021	
Prof. Roopa Patil	
	Kanade Harshada Ashok	2KL18CS026		
	Sandhya D Kumbhar	2KL18CS077		
				

