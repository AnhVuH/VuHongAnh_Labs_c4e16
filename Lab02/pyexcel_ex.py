import pyexcel

a_list_of_dictionaries = [
{
"title" : "Hom nay troi dep",
"link" :"http://dantri.com.vn/"},
{
"title" : "Hom nay troi xau",
"link" :"http://dantri.com.vn/"},
{
"title" : "Hom nay troi den",
"link" :"http://dantri.com.vn/"}
]
pyexcel.save_as(records = a_list_of_dictionaries,dest_file_name="text.xls")
