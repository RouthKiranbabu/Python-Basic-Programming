from bs4 import BeautifulSoup
import requests

source=requests.get("https://finance.yahoo.com/quote/GOOG/history?p=GOOG").text

soup=BeautifulSoup(source,'lxml')

Date=[]
Open=[]
High=[]
Low=[]
Close=[]
Adj_Close=[]
Volume=[]
OHLCAV=[]

for article in soup.find_all("td",class_="Py(10px) Ta(start) Pend(10px)"):
	Date.append(str(article.span.text))

for val in soup.find_all("td",class_="Py(10px) Pstart(10px)"):
	OHLCAV.append(str(val.span.text))

print(OHLCAV)
'''
output:
['1,148.19', '1,151.14', '1,129.62', '1,130.10', '1,130.10', '1,646,300',
 '1,141.74', '1,147.60', '1,132.73', '1,146.33', '1,146.33', '1,291,300',
  '1,150.97', '1,158.36', '1,145.77', '1,146.35', '1,146.35',
   '1,170,000', '1,146.00', '1,158.58', '1,145.00', '1,153.58',
    '1,153.58', '1,238,800', '1,146.86', '1,150.82', '1,139.40',
     '1,150.34', '1,150.34', '903,800', '1,143.99', '1,147.34',
      '1,138.78', '1,144.90', '1,144.90', '864,000', '1,143.25',
       '1,153.07', '1,139.58', '1,144.21', '1,144.21', '1,195,500',
        '1,131.22', '1,142.05', '1,130.97', '1,140.48', '1,140.48',
         '1,209,500', '1,111.80', '1,128.03', '1,107.17', '1,124.83',
          '1,124.83', '1,330,400', '1,125.17', '1,125.98', '1,111.21',
           '1,116.35', '1,116.35', '1,236,400', '1,117.80', '1,132.88',
            '1,116.14', '1,131.59', '1,131.59', '1,264,300', '1,117.41',
             '1,126.76', '1,113.86', '1,121.58', '1,121.58', '767,000',
              '1,102.24', '1,111.77', '1,098.17', '1,111.25', '1,111.25',
               '991,600', '1,098.00', '1,107.58', '1,093.70', '1,097.95',
                '1,097.95', '1,436,300', '1,076.39', '1,081.00', '1,073.37',
                 '1,080.91', '1,080.91', '1,693,200', '1,084.00',
                  '1,087.10', '1,075.29', '1,076.01', '1,076.01',
                   '1,004,300', '1,086.50', '1,092.97', '1,072.24',
                    '1,079.80', '1,079.80', '1,810,900', '1,112.66',
                     '1,114.35', '1,083.80', '1,086.35', '1,086.35',
                      '1,546,900', '1,119.61', '1,122.00', '1,111.01',
                       '1,115.52', '1,115.52', '1,395,600', '1,109.24',
                        '1,124.11', '1,108.08', '1,121.88', '1,121.88',
                         '1,947,600', '1,119.99', '1,120.12', '1,104.74',
 '1,111.42', '1,111.42', '1,262,000', '1,105.60', '1,107.00',
  '1,093.48', '1,102.33', '1,102.33', '1,338,800', '1,109.69',
   '1,116.39', '1,098.99', '1,103.60', '1,103.60', '1,386,700', 
   '1,086.28', '1,099.18', '1,086.28', '1,092.50', '1,092.50', 
   '941,600', '1,086.42', '1,092.69', '1,080.17', '1,085.35', 
   '1,085.35', '1,111,500', '1,083.64', '1,094.17', '1,080.15',
    '1,088.77', '1,088.77', '1,057,700', '1,078.00', '1,080.93',
     '1,067.54', '1,077.03', '1,077.03', '1,061,000', '1,093.98',
      '1,101.99', '1,077.60', '1,078.72', '1,078.72', '1,436,700',
       '1,072.98', '1,092.66', '1,072.32', '1,080.38', '1,080.38', 
       '1,464,200', '1,050.63', '1,070.92', '1,048.40', '1,066.04',
        '1,066.04', '1,802,400', '1,044.99', '1,047.49', '1,033.70',
         '1,044.34', '1,044.34', '1,703,200', '1,051.54', '1,053.55',
 '1,030.49', '1,042.22', '1,042.22', '2,168,400', '1,042.90', '1,056.05',
  '1,033.69', '1,053.05', '1,053.05', '2,833,500', '1,065.50', '1,065.50',
   '1,025.00', '1,036.23', '1,036.23', '5,130,600', '1,101.29', '1,109.60',
    '1,100.18', '1,103.63', '1,103.63', '1,507,800', '1,115.54', '1,123.13',
     '1,112.12', '1,117.95', '1,117.95', '951,900', '1,127.52', '1,129.10', 
     '1,108.22', '1,116.46', '1,116.46', '1,538,200', '1,134.00', '1,151.59', 
     '1,133.12', '1,134.15', '1,134.15', '1,365,000', '1,147.36', '1,149.77', 
     '1,131.66', '1,133.47', '1,133.47', '1,112,000', '1,140.50', '1,145.97',
      '1,129.22', '1,140.77', '1,140.77', '1,198,900', '1,146.75', '1,158.52',
       '1,145.89', '1,151.42', '1,151.42', '914,500', '1,148.49', '1,152.71', 
       '1,137.94', '1,149.63', '1,149.63', '1,159,800', '1,144.50',
        '1,146.80', '1,131.44', '1,138.85', '1,138.85', '1,353,300',
         '1,168.47', '1,180.15', '1,160.01', '1,162.30', '1,162.30', 
         '1,208,600', '1,164.51', '1,188.16', '1,162.84', '1,178.98', 
         '1,178.98', '1,531,400', '1,117.87', '1,171.33', '1,116.67', 
         '1,164.21', '1,164.21', '2,289,300', '1,137.21', '1,140.42', 
         '1,119.55', '1,120.44', '1,120.44', '1,836,600', '1,141.96', 
         '1,147.94', '1,122.11', '1,132.03', '1,132.03', '1,860,600', 
         '1,163.59', '1,172.60', '1,142.50', '1,164.27', '1,164.27',
          '1,314,500', '1,159.03', '1,169.66', '1,150.85', '1,162.38',
           '1,162.38', '1,185,700', '1,172.01', '1,180.42', '1,165.74', 
           '1,166.27', '1,166.27', '1,309,300', '1,180.47', '1,190.44', 
'1,161.04', '1,174.10', '1,174.10', '1,551,400', '1,166.26', '1,190.85',
 '1,166.26', '1,189.39', '1,189.39', '1,563,900', '1,173.65', '1,186.80', 
 '1,169.00', '1,185.40', '1,185.40', '1,980,700', '1,167.76', '1,174.19', 
 '1,155.00', '1,162.61', '1,162.61', '1,944,800', '1,188.05', '1,188.05',
  '1,167.18', '1,168.08', '1,168.08', '2,639,200', '1,185.00', '1,192.81',
   '1,175.00', '1,188.48', '1,188.48', '6,207,000', '1,274.00', '1,289.27',
    '1,266.30', '1,287.58', '1,287.58', '2,499,400', '1,269.00',
     '1,273.07', '1,260.32', '1,272.18', '1,272.18', '1,241,400',
      '1,264.77', '1,267.41', '1,252.03', '1,263.45', '1,263.45', 
      '1,107,300', '1,264.12', '1,268.01', '1,255.00', '1,256.00', 
      '1,256.00', '1,018,800', '1,250.69', '1,269.00', '1,246.38', 
      '1,264.55', '1,264.55', '1,319,900', '1,235.99', '1,249.09', 
      '1,228.31', '1,248.84', '1,248.84', '807,300', '1,239.18', 
      '1,242.00', '1,234.61', '1,236.37', '1,236.37', '1,331,800', 
      '1,233.00', '1,240.56', '1,227.82', '1,236.34', '1,236.34',
       '1,221,900', '1,225.00', '1,230.82', '1,220.12', '1,227.13',
        '1,227.13', '856,300', '1,218.00', '1,224.20', '1,209.11', 
        '1,221.10', '1,221.10', '1,187,400', '1,210.00', '1,218.35',
         '1,208.11', '1,217.87', '1,217.87', '933,400', '1,203.96',
          '1,207.96', '1,200.13', '1,204.62', '1,204.62', '710,200',
           '1,200.68', '1,203.79', '1,196.44', '1,202.16', '1,202.16',
            '724,600', '1,196.00', '1,202.29', '1,193.08', '1,197.25',
             '1,197.25', '876,400', '1,207.89', '1,208.69', '1,199.86', 
             '1,203.84', '1,203.84', '860,200', '1,214.99', '1,216.22',
              '1,205.03', '1,207.15', '1,207.15', '907,200', '1,205.94',
               '1,215.67', '1,204.13', '1,215.00', '1,215.00', '950,000', 
               '1,207.48', '1,216.30', '1,200.50', '1,205.92', '1,205.92',
                '1,014,300', '1,195.32', '1,201.35', '1,185.71', '1,200.49',
                 '1,200.49', '827,900', '1,184.10', '1,196.66', '1,182.00', 
                 '1,194.43', '1,194.43', '1,252,500', '1,174.90', '1,178.99',
                  '1,162.88', '1,173.31', '1,173.31', '1,269,900', '1,171.54', 
                  '1,171.56', '1,159.43', '1,168.49', '1,168.49', '961,700', 
                  '1,185.50', '1,187.56', '1,159.37', '1,173.02', '1,173.02',
                   '1,400,200', '1,198.53', '1,202.83', '1,176.72', '1,184.62',
 '1,184.62', '1,901,200', '1,196.93', '1,206.40', '1,187.04', '1,193.00', '1,193.00',
  '1,496,800', '1,226.32', '1,230.00', '1,202.82', '1,205.50', '1,205.50', 
  '1,714,200', '1,216.00', '1,231.79', '1,213.15', '1,231.54', '1,231.54', 
  '1,204,000', '1,197.35', '1,227.14', '1,196.17', '1,223.97', '1,223.97', 
  '2,227,400', '1,188.81', '1,200.00', '1,185.87', '1,198.85', '1,198.85', 
  '1,520,700', '1,183.30', '1,190.00', '1,177.42', '1,184.26', '1,184.26', 
  '1,292,600', '1,193.38', '1,196.57', '1,182.61', '1,184.46', '1,184.46',
   '2,461,800', '1,194.51', '1,197.88', '1,184.48', '1,185.55', '1,185.55',
    '1,172,800', '1,200.65', '1,200.93', '1,191.94', '1,193.32', '1,193.32',
     '1,435,900', '1,178.26', '1,200.00', '1,178.26', '1,193.20', '1,193.20',
      '2,013,100', '1,144.45', '1,176.19', '1,144.45', '1,175.76', '1,175.76',
       '1,719,200', '1,126.73', '1,147.08', '1,123.30', '1,142.32', '1,142.32'
       , '1,212,400', '1,155.72', '1,156.76', '1,134.91', '1,143.30', '1,143.30', 
       '1,166,600', '1,162.49', '1,167.57', '1,155.49', '1,157.86', '1,157.86'
       , '1,099,300', '1,150.06', '1,169.61', '1,146.19', '1,162.03', '1,162.03',
        '1,443,200', '1,146.99', '1,158.28', '1,130.69', '1,147.80', '1,147.80', 
        '1,446,000', '1,124.90', '1,142.97', '1,124.75', '1,140.99', '1,140.99',
         '1,450,300', '1,111.30', '1,127.65', '1,111.01', '1,119.92', '1,119.92',
          '1,542,500', '1,106.95', '1,117.98', '1,101.00', '1,116.05', '1,116.05',
           '968,400']'''





