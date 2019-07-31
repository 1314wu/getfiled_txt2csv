import  re
import  sys
import  os
def readContent():
    source_path=sys.argv[1]
    f=open(source_path,'r')

    resul_name=sys.argv[2]


    file_csv=open(resul_name,'w')
    file_csv.write('bitrate,')
    file_csv.write('vmaf,')
    file_csv.write('ssim,')
    file_csv.write('psnr,')
    file_csv.write('\n')

    strlins_txt = f.readlines()
    list0=str(strlins_txt[0])

    for lines in strlins_txt:
        #str_dec=lines.decode()
        #print(str_dec)
        br=re.findall("br\":\s*\[(\d+\.\d+)\],\s*\"vmaf\":\s*\[(\d+.\d+)\],\s\"ssim\":\s*\[(\d+.\d+)\],\s\"psnr\":\s\[(\d+.\d+)\]",lines)
        file_csv.write(br[0][0])
        file_csv.write(',')
        file_csv.write(br[0][1])
        file_csv.write(',')
        file_csv.write(br[0][2])
        file_csv.write(',')
        file_csv.write(br[0][3])
        file_csv.write('\n')






'''str_input='\"str[100.13]\"'
print(str_input)                #处理不确定字符串中是否有空格的情况
opt=re.findall("\"str(?:\s|)\[(\d+.\d+)\]\"",str_input)'''




readContent()

