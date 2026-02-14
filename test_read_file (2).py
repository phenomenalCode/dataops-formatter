import unittest as ut
import sys
import os


sys.path.append("..")
import read_file as rf

class TestReadFile(ut.TestCase):

	def test_set_column_pad_values(self):
		sm = 15
		med = 25
		lg = 50
		#function to change the default column pad values
		rf.set_column_pad_values(sm,med,lg)
		self.assertTrue(rf.sm_column_pad==sm,f"small column width not set: {rf.sm_column_pad}!={sm}") 
		self.assertTrue(rf.med_column_pad==med,f"medium column width not set: {rf.med_column_pad}!={med}") 
		self.assertTrue(rf.lg_column_pad==lg,f"large column width not set: {rf.lg_column_pad}!={lg}")
	#end function

	#should refactor this test with known values and expected values
	#instead of repeated the tested function login
	def test_pad_value_column_width(self): 		
		#calculates and pads to the end of value, a number of empty spaces
		value_sm = "Hello World!"
		value_med = "This is a 45 character string for your request."
		value_lg =  "Here is a 60 character string to fulfill your request. I hope this meets your needs!"
		actual_s = rf.pad_value_column_width(value_sm)
		actual_m = rf.pad_value_column_width(value_med)
		actual_l =  rf.pad_value_column_width(value_lg)
		expected_s = "Hello World!        "
		expected_m = "This is a 45 character string for your request.   "                                                        
		expected_l = "Here is a 60 character string to fulfill your request. I hope this meets your needs!                "

		self.assertTrue(actual_s==expected_s, f"small column width not valid: {actual_s}!={expected_s}") 
		self.assertTrue(actual_m==expected_m, f"medium column width not set: {actual_m}!={expected_m}") 
		self.assertTrue(actual_l==expected_l, f"large column width not set: {actual_l}!={expected_l}") 
	#end function
			
	#setup known values for header input and expected return
	def test_format_table_header(self): 
		row = "iam a horse,iam a horse,iam a horse"
		expected_row = "iam_a_horse         iam_a_horse         iam_a_horse         "
		actual_row = rf.format_table_header(row)
		print(f'actual_row= {actual_row}')	
		self.assertTrue(len(expected_row)==len(actual_row), f"expected result not met: {len(expected_row)}!={len(actual_row)}")
		self.assertTrue(expected_row==actual_row, f"expected result not met: {expected_row}!={actual_row}")
	#end function

	def test_format_table_row(self): 
		row = "iam a horse,iam a horse,iam a horse"
		expected_row = "iam a horse         iam a horse         iam a horse         "
		actual_row = rf.format_table_row(row)
		print(f'actual_row= {actual_row}')	
		self.assertTrue(len(expected_row)==len(actual_row), f"expected result not met: {len(expected_row)}!={len(actual_row)}")
		self.assertTrue(expected_row==actual_row, f"expected result not met: {expected_row}!={actual_row}")
	#end function

	def test_write_table_line(self):
		pass
		#rf.write_table_line(f,input):
		assert False, "test not written yet"
	#end function


#end class

if __name__ == '__main__':
    ut.main()