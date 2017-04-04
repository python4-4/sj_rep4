Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> somebody=raw_input("Enter your name:")
Enter your name:
>>> 
>>> 


>>> 


>>> 

>>> 


>>> 

>>> 
>>> AAA

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    AAA
NameError: name 'AAA' is not defined
>>> AAA

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    AAA
NameError: name 'AAA' is not defined
>>> somebody=raw_input ("
		    
SyntaxError: EOL while scanning string literal
>>> Somebody=raw_input("Enter your name :")
Enter your name :AAA
>>> print "hi!", somebody, "How are you today?"
hi!  How are you today?
>>> somebody = raw_input ("Enter your name :")
Enter your name :AAA
>>> print "hi!", somebody, "Hpw are you ?"
hi! AAA Hpw are you ?
>>> print"I",
I
>>> my_file=open('C:\Temp\sample.txt', 'w')
>>> my_file.write ("1.Wake up")
>>> my_file.write("\n2.Brush")
>>> my_file.write ("\n3. Eat")
>>> my_file.close()
>>> my_file = open('C:\Temp\sample.txt', 'r')
>>> print my_file.read()
1.Wake up
2.Brush
3. Eat
>>> my_file = open('C:\Temp\HncDownload\update.log', 'r')
>>> print my_file.readline()
[Done]

>>> my_file.seek(0)
>>> print my_file.readlines()
['[Done]\n', '0908_145101.6726=End to (None)\n', '0909_102653.2620=End to (None)\n', '0912_090442.0357=End to (None)\n', '0912_121425.4045=End to (None)\n', '0912_132553.7755=End to (None)\n', '0919_090945.3816=End to (None)\n', '0919_184501.5313=End to (None)\n', '0920_180441.1545=End to (None)\n', '0921_102430.6450=End to (None)\n', '0922_121711.2463=End to (None)\n', '0922_150437.4268=End to (None)\n', '0923_104115.5531=End to (None)\n', '0923_110310.3896=End to (None)\n', '0926_094250.9167=End to (None)\n', '0926_132742.9576=End to (None)\n', '0928_102345.7333=End to (None)\n', '0929_101339.7550=End to (None)\n', '0930_102658.5443=End to (None)\n', '0930_183959.3896=End to (None)\n', '1001_125217.1031=End to (None)\n', '1005_102538.0351=End to (None)\n', '1006_121052.9233=End to (None)\n', '1006_145637.2817=End to (None)\n', '1007_114838.1459=End to (None)\n', '1010_133945.1420=End to (None)\n', '1012_101720.4909=End to (None)\n', '1012_131105.6560=End to (None)\n', '1013_145505.3860=End to (None)\n', '1014_102614.3968=End to (None)\n', '1024_091222.2609=End to (None)\n', '1024_132519.9119=End to (None)\n', '1025_180456.3271=End to (None)\n', '1026_102711.2514=End to (None)\n', '1026_183003.5500=End to (None)\n', '1027_121146.7261=End to (None)\n', '1027_145626.9843=End to (None)\n', '1031_091644.0067=End to (None)\n', '1031_133216.7656=End to (None)\n', '1101_180803.4119=End to (None)\n', '1102_102947.1624=End to (None)\n', '1103_121353.5503=End to (None)\n', '1104_102917.7537=End to (None)\n', '1107_085931.9909=End to (None)\n', '1109_102911.9489=End to (None)\n', '1109_125149.3031=End to (None)\n', '1109_222902.1490=End to (None)\n', '1110_121014.0202=End to (None)\n', '1110_150249.0885=End to (None)\n', '1111_102701.3729=End to (None)\n', '1114_092631.6640=End to (None)\n', '1116_102539.7116=End to (None)\n', '1116_184533.9223=End to (None)\n', '1117_121748.2503=End to (None)\n', '1118_102426.9970=End to (None)\n', '1121_094549.1010=End to (None)\n', '1123_125651.0481=End to (None)\n', '1124_145927.2758=End to (None)\n', '1128_091525.1918=End to (None)\n', '1201_131747.9654=End to (None)\n', '1201_145557.7885=End to (None)\n', '1202_102801.6400=End to (None)\n', '1205_095106.8104=End to (None)\n', '1205_123922.1806=End to (None)\n', '1207_102853.6434=End to (None)\n', '1207_104234.5637=End to (None)\n', '1208_145525.3236=End to (None)\n', '1209_102550.2552=End to (None)\n', '1214_113137.8203=End to (None)\n', '1214_175438.3590=End to (None)\n', '0121_180401.2057=End to (None)\n', '0302_092625.3851=End to (None)\n', '0302_103444.8765=End to (None)\n', '0302_115848.1565=End to (None)\n', '0302_132054.6343=End to (None)\n', '0302_144319.9381=End to (None)\n', '0303_092401.6598=End to (None)\n', '0306_085822.4310=End to (None)\n', '0306_092911.1611=End to (None)\n', '0306_103429.7706=End to (None)\n', '0306_131525.1595=End to (None)\n', '0307_120218.6402=End to (None)\n', '0307_155956.6373=End to (None)\n', '0308_090921.2719=End to (None)\n', '0308_104851.2390=End to (None)\n', '0308_131137.1272=End to (None)\n', '0308_150244.4096=End to (None)\n', '0308_163506.8250=End to (None)\n', '0309_090202.0172=End to (None)\n', '0309_120233.7214=End to (None)\n', '0310_091011.1554=End to (None)\n', '0310_103504.4660=End to (None)\n', '0310_150908.2130=End to (None)\n', '0310_162807.4884=End to (None)\n', '0313_090532.4676=End to (None)\n', '0313_102307.3659=End to (None)\n', '0313_115407.7111=End to (None)\n', '0313_132623.0375=End to (None)\n', '0313_145131.3620=End to (None)\n', '0313_163545.7015=End to (None)\n', '0314_120315.6282=End to (None)\n', '0314_145402.5914=End to (None)\n', '0314_163239.0003=End to (None)\n', '0314_175942.8597=End to (None)\n', '0315_083757.6016=End to (None)\n', '0315_103044.0228=End to (None)\n', '0315_132234.2777=End to (None)\n', '0315_144515.8600=End to (None)\n', '0315_163732.5613=End to (None)\n', '0316_091716.6264=End to (None)\n', '0316_103225.0471=End to (None)\n', '0316_115237.4302=End to (None)\n', '0316_132536.3605=End to (None)\n', '0316_145459.3499=End to (None)\n', '0317_090122.4133=End to (None)\n', '0317_103057.7138=End to (None)\n', '0317_151829.9405=End to (None)\n', '0317_162807.4051=End to (None)\n', '0320_084908.1858=End to (None)\n', '0320_102617.7564=End to (None)\n', '0320_115224.7360=End to (None)\n', '0320_162851.5393=End to (None)\n', '0321_102122.8681=End to (None)\n', '0321_120330.4962=End to (None)\n', '0321_131929.1011=End to (None)\n', '0321_162407.7972=End to (None)\n', '0322_085824.8783=End to (None)\n', '0322_103538.1845=End to (None)\n', '0322_145216.7726=End to (None)\n', '0322_163059.6928=End to (None)\n', '0323_091015.8152=End to (None)\n', '0323_102349.4457=End to (None)\n', '0323_115533.4941=End to (None)\n', '0323_133409.1513=End to (None)\n', '0324_090903.2945=End to (None)\n', '0324_102736.6706=End to (None)\n', '0324_114457.0042=End to (None)\n', '0324_162411.9316=End to (None)\n', '0327_090715.0354=End to (None)\n', '0327_103126.7068=End to (None)\n', '0327_115629.2639=End to (None)\n', '0327_132230.4599=End to (None)\n', '0328_102702.8649=End to (None)\n', '0328_115720.9434=End to (None)\n', '0328_163555.2430=End to (None)\n', '0329_085922.8740=End to (None)\n', '0329_103135.1974=End to (None)\n', '0329_131445.9433=End to (None)\n', '0329_144818.1677=End to (None)\n', '0330_102623.5113=End to (None)\n', '0330_120040.9902=End to (None)\n', '0331_085541.4306=End to (None)\n', '0331_102100.6803=End to (None)\n', '0331_145329.7222=End to (None)\n', '0331_150450.4061=End to (None)\n', '0331_162707.7243=End to (None)\n', '0403_085851.1494=End to (None)\n', '0403_102824.8051=End to (None)\n', '0403_115732.7948=End to (None)\n', '0403_125806.1358=End to (None)\n', '0403_163602.8740=End to (None)\n', '0404_120132.4825=End to (None)\n', '0404_133618.3046=End to (None)\n', '0404_140444.3096=End to (None)\n', '[LastLog]\n', 'Action=None\n', 'Key=0404_140451.7937\n', '[None]\n', '0908_145101.7039=Begin from (Done)\n', '0908_145109.9643=End to (Off)\n', '0909_102653.2776=Begin from (Done)\n', '0909_102702.8559=End to (Off)\n', '0912_090442.2232=Begin from (Done)\n', '0912_090452.0514=End to (Off)\n', '0912_121425.6077=Begin from (Done)\n', '0912_121436.0609=End to (Off)\n', '0912_132553.7755_0=Begin from (Done)\n', '0912_132604.0880=End to (Off)\n', '0919_090945.4726=Begin from (Done)\n', '0919_090958.5402=End to (Off)\n', '0919_184501.5313_0=Begin from (Done)\n', '0919_184509.3752=End to (Off)\n', '0920_180441.3923=Begin from (Done)\n', '0920_180458.1372=End to (Off)\n', '0921_102430.6450_0=Begin from (Done)\n', '0921_102437.3326=End to (Off)\n', '0922_121711.2834=Begin from (Done)\n', '0922_121719.1478=End to (Off)\n', '0922_150437.5013=Begin from (Done)\n', '0922_150446.0376=End to (Off)\n', '0923_104115.5885=Begin from (Done)\n', '0923_104141.9864=End to (Off)\n', '0923_110310.3906=Begin from (Done)\n', '0923_110316.3143=End to (Off)\n', '0926_094250.9324=Begin from (Done)\n', '0926_094259.2294=End to (Off)\n', '0926_132742.9576_0=Begin from (Done)\n', '0926_132750.4577=End to (Off)\n', '0928_102345.7343=Begin from (Done)\n', '0928_102351.8139=End to (Off)\n', '0929_101339.7560=Begin from (Done)\n', '0929_101347.3744=End to (Off)\n', '0930_102658.5443_0=Begin from (Done)\n', '0930_102707.2319=End to (Off)\n', '0930_183959.4211=Begin from (Done)\n', '0930_184007.0476=End to (Off)\n', '1001_125217.1491=Begin from (Done)\n', '1001_125224.5895=End to (Off)\n', '1005_102538.1288=Begin from (Done)\n', '1005_102548.0508=End to (Off)\n', '1006_121052.9233_0=Begin from (Done)\n', '1006_121103.1578=End to (Off)\n', '1006_145637.3286=Begin from (Done)\n', '1006_145646.6099=End to (Off)\n', '1007_114838.1599=Begin from (Done)\n', '1007_114845.2988=End to (Off)\n', '1010_133945.2710=Begin from (Done)\n', '1010_133953.0731=End to (Off)\n', '1012_101720.5378=Begin from (Done)\n', '1012_101731.3973=End to (Off)\n', '1012_131105.7412=Begin from (Done)\n', '1012_131116.2719=End to (Off)\n', '1013_145505.4384=Begin from (Done)\n', '1013_145513.2179=End to (Off)\n', '1014_102614.3978=Begin from (Done)\n', '1014_102619.9436=End to (Off)\n', '1024_091222.2609_0=Begin from (Done)\n', '1024_091228.2165=End to (Off)\n', '1024_132519.9129=Begin from (Done)\n', '1024_132526.0023=End to (Off)\n', '1025_180456.3271_0=Begin from (Done)\n', '1025_180504.5147=End to (Off)\n', '1026_102711.2514_0=Begin from (Done)\n', '1026_102719.4703=End to (Off)\n', '1026_183003.5500_0=Begin from (Done)\n', '1026_183011.9565=End to (Off)\n', '1027_121146.7261_0=Begin from (Done)\n', '1027_121153.1428=End to (Off)\n', '1027_145626.9843_0=Begin from (Done)\n', '1027_145635.1407=End to (Off)\n', '1031_091644.0223=Begin from (Done)\n', '1031_091652.7100=End to (Off)\n', '1031_133216.7666=Begin from (Done)\n', '1031_133222.5537=End to (Off)\n', '1101_180803.4119_0=Begin from (Done)\n', '1101_180811.6932=End to (Off)\n', '1102_102947.1624_0=Begin from (Done)\n', '1102_102955.7719=End to (Off)\n', '1103_121353.5503_0=Begin from (Done)\n', '1103_121402.8004=End to (Off)\n', '1104_102917.7537_0=Begin from (Done)\n', '1104_102925.8789=End to (Off)\n', '1107_085932.0065=Begin from (Done)\n', '1107_085940.9598=End to (Off)\n', '1109_102911.9499=Begin from (Done)\n', '1109_102917.7386=End to (Off)\n', '1109_125149.3031_0=Begin from (Done)\n', '1109_125155.3203=End to (Off)\n', '1109_222902.1490_0=Begin from (Done)\n', '1109_222910.1490=End to (Off)\n', '1110_121014.0202_0=Begin from (Done)\n', '1110_121022.6766=End to (Off)\n', '1110_150249.1041=Begin from (Done)\n', '1110_150256.9167=End to (Off)\n', '1111_102701.3739=Begin from (Done)\n', '1111_102707.1696=End to (Off)\n', '1114_092631.6650=Begin from (Done)\n', '1114_092637.6982=End to (Off)\n', '1116_102539.7126=Begin from (Done)\n', '1116_102545.2370=End to (Off)\n', '1116_184533.9233=Begin from (Done)\n', '1116_184541.1085=End to (Off)\n', '1117_121748.2503_0=Begin from (Done)\n', '1117_121755.2573=End to (Off)\n', '1118_102427.0267=Begin from (Done)\n', '1118_102433.1194=End to (Off)\n', '1121_094549.1020=Begin from (Done)\n', '1121_094554.6794=End to (Off)\n', '1123_125651.0481_0=Begin from (Done)\n', '1123_125657.3691=End to (Off)\n', '1124_145927.2758_0=Begin from (Done)\n', '1124_145933.5188=End to (Off)\n', '1128_091525.1928=Begin from (Done)\n', '1128_091531.3433=End to (Off)\n', '1201_131748.0815=Begin from (Done)\n', '1201_131755.0585=End to (Off)\n', '1201_145557.8255=Begin from (Done)\n', '1201_145604.7734=End to (Off)\n', '1202_102801.6771=Begin from (Done)\n', '1202_102808.7901=End to (Off)\n', '1205_095106.8674=Begin from (Done)\n', '1205_095115.6486=End to (Off)\n', '1205_123922.1816=Begin from (Done)\n', '1205_123930.0102=End to (Off)\n', '1207_102853.8486=Begin from (Done)\n', '1207_102904.0831=End to (Off)\n', '1207_104234.5915=Begin from (Done)\n', '1207_104244.4477=End to (Off)\n', '1208_145525.3236_0=Begin from (Done)\n', '1208_145531.2209=End to (Off)\n', '1209_102550.2552_0=Begin from (Done)\n', '1209_102558.4584=End to (Off)\n', '1214_113137.8213=Begin from (Done)\n', '1214_113145.3832=End to (Off)\n', '1214_175438.3601=Begin from (Done)\n', '1214_175449.8004=End to (Off)\n', '0121_180401.2057_0=Begin from (Done)\n', '0121_180411.2849=End to (Off)\n', '0302_092625.4848=Begin from (Done)\n', '0302_092644.5163=End to (Off)\n', '0302_103444.9547=Begin from (Done)\n', '0302_103456.0329=End to (Off)\n', '0302_115848.2346=Begin from (Done)\n', '0302_115859.5629=End to (Off)\n', '0302_132054.6498=Begin from (Done)\n', '0302_132105.1656=End to (Off)\n', '0302_144320.1100=Begin from (Done)\n', '0302_144330.2976=End to (Off)\n', '0303_092401.7378=Begin from (Done)\n', '0303_092412.0817=End to (Off)\n', '0306_085822.4778=Begin from (Done)\n', '0306_085833.1342=End to (Off)\n', '0306_092911.1767=Begin from (Done)\n', '0306_092920.7081=End to (Off)\n', '0306_103429.8174=Begin from (Done)\n', '0306_103439.3175=End to (Off)\n', '0306_131525.3866=Begin from (Done)\n', '0306_131536.4622=End to (Off)\n', '0307_120218.7219=Begin from (Done)\n', '0307_120227.9796=End to (Off)\n', '0307_155956.7154=Begin from (Done)\n', '0307_160008.0014=End to (Off)\n', '0308_090921.2719_0=Begin from (Done)\n', '0308_090930.6939=End to (Off)\n', '0308_104851.3015=Begin from (Done)\n', '0308_104902.9279=End to (Off)\n', '0308_131137.1741=Begin from (Done)\n', '0308_131147.6689=End to (Off)\n', '0308_150244.4409=Begin from (Done)\n', '0308_150253.8628=End to (Off)\n', '0308_163506.8718=Begin from (Done)\n', '0308_163517.1375=End to (Off)\n', '0309_090202.0642=Begin from (Done)\n', '0309_090214.1111=End to (Off)\n', '0309_120233.7996=Begin from (Done)\n', '0309_120244.4872=End to (Off)\n', '0310_091011.2114=Begin from (Done)\n', '0310_091019.5565=End to (Off)\n', '0310_103504.4980=Begin from (Done)\n', '0310_103511.3088=End to (Off)\n', '0310_150908.2140=Begin from (Done)\n', '0310_150916.2239=End to (Off)\n', '0310_162807.4894=Begin from (Done)\n', '0310_162816.5001=End to (Off)\n', '0313_090532.4676_0=Begin from (Done)\n', '0313_090544.2368=End to (Off)\n', '0313_102307.3669=Begin from (Done)\n', '0313_102314.8404=End to (Off)\n', '0313_115407.7121=Begin from (Done)\n', '0313_115417.5917=End to (Off)\n', '0313_132623.0843=Begin from (Done)\n', '0313_132630.4496=End to (Off)\n', '0313_145131.3943=Begin from (Done)\n', '0313_145139.3777=End to (Off)\n', '0313_163545.7513=Begin from (Done)\n', '0313_163552.9571=End to (Off)\n', '0314_120315.6952=Begin from (Done)\n', '0314_120324.0772=End to (Off)\n', '0314_145402.6444=Begin from (Done)\n', '0314_145410.3849=End to (Off)\n', '0314_163239.0023=Begin from (Done)\n', '0314_163245.7146=End to (Off)\n', '0314_175942.9328=Begin from (Done)\n', '0314_175950.3080=End to (Off)\n', '0315_083757.6827=Begin from (Done)\n', '0315_083806.6260=End to (Off)\n', '0315_103044.0258=Begin from (Done)\n', '0315_103050.8396=End to (Off)\n', '0315_132234.5308=Begin from (Done)\n', '0315_132243.5392=End to (Off)\n', '0315_144516.0501=Begin from (Done)\n', '0315_144533.9858=End to (Off)\n', '0315_163732.7644=Begin from (Done)\n', '0315_163744.6707=End to (Off)\n', '0316_091716.6732=Begin from (Done)\n', '0316_091728.8608=End to (Off)\n', '0316_103225.0940=Begin from (Done)\n', '0316_103235.1407=End to (Off)\n', '0316_115237.4614=Begin from (Done)\n', '0316_115247.6021=End to (Off)\n', '0316_132536.5011=Begin from (Done)\n', '0316_132547.3919=End to (Off)\n', '0316_145459.4281=Begin from (Done)\n', '0316_145511.0532=End to (Off)\n', '0317_090122.4143=Begin from (Done)\n', '0317_090132.0081=End to (Off)\n', '0317_103057.7148=Begin from (Done)\n', '0317_103110.2697=End to (Off)\n', '0317_151830.0030=Begin from (Done)\n', '0317_151841.0969=End to (Off)\n', '0317_162807.5457=Begin from (Done)\n', '0317_162816.3895=End to (Off)\n', '0320_084908.1878=Begin from (Done)\n', '0320_084914.1140=End to (Off)\n', '0320_102617.8345=Begin from (Done)\n', '0320_102629.8346=End to (Off)\n', '0320_115224.8766=Begin from (Done)\n', '0320_115234.5486=End to (Off)\n', '0320_162851.5393_0=Begin from (Done)\n', '0320_162900.7425=End to (Off)\n', '0321_102122.9306=Begin from (Done)\n', '0321_102135.7745=End to (Off)\n', '0321_120330.5431=Begin from (Done)\n', '0321_120340.1837=End to (Off)\n', '0321_131929.1011_0=Begin from (Done)\n', '0321_131938.4762=End to (Off)\n', '0321_162407.8282=Begin from (Done)\n', '0321_162416.0000=End to (Off)\n', '0322_085824.9584=Begin from (Done)\n', '0322_085832.3396=End to (Off)\n', '0322_103538.1855=Begin from (Done)\n', '0322_103544.9173=End to (Off)\n', '0322_145216.7736=Begin from (Done)\n', '0322_145222.5347=End to (Off)\n', '0322_163059.6948=Begin from (Done)\n', '0322_163105.6666=End to (Off)\n', '0323_091015.8162=Begin from (Done)\n', '0323_091023.5467=End to (Off)\n', '0323_102349.4467=Begin from (Done)\n', '0323_102356.8620=End to (Off)\n', '0323_115533.5311=Begin from (Done)\n', '0323_115539.9427=End to (Off)\n', '0323_133409.1523=Begin from (Done)\n', '0323_133415.4107=End to (Off)\n', '0324_090903.2955=Begin from (Done)\n', '0324_090911.3802=End to (Off)\n', '0324_102736.7076=Begin from (Done)\n', '0324_102745.6146=End to (Off)\n', '0324_114457.0403=Begin from (Done)\n', '0324_114503.8611=End to (Off)\n', '0324_162411.9327=Begin from (Done)\n', '0324_162419.3499=End to (Off)\n', '0327_090715.0374=Begin from (Done)\n', '0327_090721.6741=End to (Off)\n', '0327_103126.7068_0=Begin from (Done)\n', '0327_103134.9570=End to (Off)\n', '0327_115629.2639_0=Begin from (Done)\n', '0327_115637.6391=End to (Off)\n', '0327_132230.4599_0=Begin from (Done)\n', '0327_132238.5694=End to (Off)\n', '0328_102702.9489=Begin from (Done)\n', '0328_102711.6001=End to (Off)\n', '0328_115720.9444=Begin from (Done)\n', '0328_115727.6932=End to (Off)\n', '0328_163555.3055=Begin from (Done)\n', '0328_163605.0556=End to (Off)\n', '0329_085922.8740_0=Begin from (Done)\n', '0329_085934.0148=End to (Off)\n', '0329_103135.3067=Begin from (Done)\n', '0329_103147.2600=End to (Off)\n', '0329_131445.9433_0=Begin from (Done)\n', '0329_131456.8965=End to (Off)\n', '0329_144818.2770=Begin from (Done)\n', '0329_144828.5271=End to (Off)\n', '0330_102623.5523=Begin from (Done)\n', '0330_102630.9565=End to (Off)\n', '0330_120040.9912=Begin from (Done)\n', '0330_120047.0171=End to (Off)\n', '0331_085541.4316=Begin from (Done)\n', '0331_085547.5369=End to (Off)\n', '0331_102100.6813=Begin from (Done)\n', '0331_102106.5584=End to (Off)\n', '0331_145329.7232=Begin from (Done)\n', '0331_145336.7572=End to (Off)\n', '0331_150450.4071=Begin from (Done)\n', '0331_150456.5134=End to (Off)\n', '0331_162707.7243_0=Begin from (Done)\n', '0331_162716.2400=End to (Off)\n', '0403_085851.2155=Begin from (Done)\n', '0403_085859.8161=End to (Off)\n', '0403_102825.0082=Begin from (Done)\n', '0403_102837.3496=End to (Off)\n', '0403_115732.8261=Begin from (Done)\n', '0403_115743.6386=End to (Off)\n', '0403_125806.2608=Begin from (Done)\n', '0403_125819.5289=End to (Off)\n', '0403_163603.0146=Begin from (Done)\n', '0403_163611.7727=End to (Off)\n', '0404_120132.5796=Begin from (Done)\n', '0404_120145.2346=End to (Off)\n', '0404_133618.3656=Begin from (Done)\n', '0404_133627.2579=End to (Off)\n', '0404_140444.3577=Begin from (Done)\n', '0404_140451.7937=End to (Off)\n']
>>> import urllib2
>>> file=urllib2.urlopen('https://wordpress.org/plugins/about/readme.txt')
>>> message=file read()
SyntaxError: invalid syntax
>>> file = urllib2.urlopen('https://courses.cs.washington.edu/courses/cse326/02wi/homework/hw5/README-1.txt')
>>> message=file.read()
>>> print message
----------------------
Command Line Arguments
----------------------

Example:  ./word-count -b -sort SelectionSort -suf < textfile

-b | -a | -s
  (required) Specifies the type of tree for storing (word, count) pair
  possible trees are Binary search tree, Avl tree, and Splay tree

    -b - Count frequencies using an unbalanced binary search tree 
    -a - Count frequencies using an AVL tree 
    -s - Count frequencies using a splay tree 

-sort SelectionSort | MergeSort | HeapSort
  (optional) Specifies the type of sort.  
  If -sort is omitted, HeapSort is used

-suf
  (optional) Turns on suffix checker

-------------------------
Design Decisions & Issues
-------------------------
Since we stereotype against english majors, let's avoid writing this in an
essay format...

Q.  The original BinarySearchTree::Insert() resolves key collosion by
overwriting the old value with the new value.  How does the modified insert
functions resolve key collosions?

A.  The modified insert functions resolve key collosions by adding the new
value to the old value.  For example, if there exists a key K with a value 3,
and we wanted to insert a key K with value 2, the Insert function would change
the value to 3+2=5.  For our word-count, every key is inserted with a value 1.
However, it's easy to see that the insert functions allow different changes to
be made to the existing key-value tree.
    Consequently, the + operator must be overloaded for the ValueType.  


Q.  What is the relationship between the AVLNode class and the BSTNode class?

A.  The AVLNode is-a BSTNode.  Since the AVLTree inherits and uses many
methods from the BinarySearchTree (which operates on BSTNodes), the nodes used
by the AVLTree must be compatible.
    The difference between AVLNode and its ancestor is that each AVLNode
remembers its height information.   This is because the AVL rotations
frequently compares the height of its subtrees, and it would be inefficent if
we had to recursively calculate such info.



Class Hierachy

		|-------------------------|             |------------|
                |     BinarySearchTree    |--has-a----->|   BSTNode  |
                |-------------------------|             |------------|
                           ^    ^                           ^  ^
                          /      \                          |  |
                       is-a     is-a                        |  |
                        /          \                        |  |
                       /           |--------------|         |  |
                      /            |  SplayTree   |-has-a---|  |
                     /             |--------------|            |
                    /                                        is-a 
                   /                                           |
    |----------------|                                  |------------|
    |     AVLTree    |--has-a-------------------------->| AVLNode    |
    |----------------|                                  |------------|
   



Q.  There is no SplayNode class.  Why does SplayTree use BSTNodes?

A.  The SplayTree class uses BSTNode, while the AVLTree uses AVLNode. The idea
is that AVLTree needs to keep track of the height information. On the other
hand, SplayTree doesn't need to have height information. This is very similar
to BSTNode class, so there's no need to make a SplayNode class.


Q.  What are the similarities and differences between AVLTree rotation methods
and SplayTree rotation methods?  Why are they not methods of BinarySearchTree
class or the node classes?

A.  They are basically the same. However, for the AVLTree rotations, they need
to update the height information while the SplayTree's methods don't. These
methods could have been methods of BinarySearchTree, so that AVLTree and
SplayTree can inherit them; however, BST doesn't use rotation at all. We then
came to the decision of making each of the AVLTree, SplayTree different
rotation methods.


Q.  The Heap class does not allocate any memory--it shares the data.  Why?

A.  It makes it faster =)


Q.  Sort() is currently a method of HeapSort.  The alternative is to define an
external HeapSort() function that is a friend of the Heap class--HeapSort()
still needs to call the PercDown() function.  Why did we choose to make
HeapSort a function inside the Heap class?

A.  We think that our special(ized) Heap should know how to sort itself. :)


-----------------------
Word Frequency Analysis
-----------------------

These were the steps to the process:
    1 ) run word-count on each essay
    2 ) record the frequency for the top 28 most frequent words and
	take a subtotal for each (this will be the total number of
	'relevant' words in each literature)
    3 ) isolate the words that made it to top 7 (there were 10), and
	take their percentage with respect to the subtotals
    4 ) anaylze by comparing the percentages

Of the 10 words to anaylze, words not used at predictable frequencies by Sir
Francis Bacon (is, in, you) were ignored.  That left 6 words that are used
at predictable frequencies by Bacon (of, the, and, that, to, a), and 1 word
that is not used significantly by Bacon (I).  Two of the 6 words used
frequently and predictably by Bacon (to, a) were used just as frequent
and predictable in Hamlet and All's Well that Ends Well.  On the other hand,
the 4 remaining words (of, the, and, that), which also happens to be the words
used the most frequent by Bacon, are used at only 1/2 to 2/3 the frequency by
the author of Hamlet and All's Well that Ends Well.  The minor similarities
hardly make up for the major differeces.  Based on the above analysis, we 
conclude that Bacon wrote neither of Shakespeare's plays.
	

---------
Profiling
---------

Our expected performance bottlenecks for the word-count program are...
	+ the Splay operation for SplayTree
	+ the insertHelp function for AVL, and
	+ the PercolateDown operation for Heap
We chose these to be the bottlenecks because we assumed the function call
frequencies and costs. However, it turned out that some of these are not huge
bottlenecks at all. For example, Splay funtion doesn't take as much time as we
thought.  Words that are inserted frequently don't take so much rotations
because they are already close to the root.


  %   cumulative   self              self     total           
 time   seconds   seconds    calls  ns/call  ns/call  name    

  1.05      1.55     0.02                             SplayTree<>::Splay()
  4.26      0.45     0.10	                      AVLTree<>::insertHelp()
  1.28      1.76     0.03                             Heap::percDown()


The gprof results show that, in general standard I/O operations takes up most 
of the runtime:


index % time    self  children    called     name
[2]     24.3    0.05    0.52   45429         next_token()
[3]     20.0    0.05    0.42                 operator<<()


Even though each word is only read/printed once, we think the cause for I/O
as a bottleneck is its huge constant overhead (which much exceeds the log n
tree operations)

For specific choice of trees and input, namely bst tree with word.txt as
input, the biggest bottleneck was string operations and FindNode() function. 
The cause is that the pre-sorted words created an unbalanced binary search
tree, requiring a complete traversal of a linked-list-like data structure
everytime a word is inserted.  At each node visited during the traversal,
FindNode compares the string keys.


index % time    self  children    called     name
                                                 <spontaneous>
[1]     75.6  167.51  533.04                 std::string::compare()
               99.37  235.36 3408496094/3408541521     std::string::size()
               35.05   81.63 1704248047/1704293468     std::string::data() 
               81.63    0.00 1704248047/2523092351     std::string::_M_data()


Another significant operation which we overlooked (for the AVLTree) is the
UpdateHeight function (which actually took 3.8 percent of the run time).

  %   cumulative   self              self     total           
 time   seconds   seconds    calls  ns/call  ns/call  name    
  3.83      0.54     0.09                             AVLTree<>::updateHeight()


--------------------
Algorithmic Analysis
--------------------

From our "SelectionSortSort vs. HeapSort" plot, we can see that when N is greater than
8000, selectionsort function grows faster than heapsort function. This confroms our knowledge
that heap sort has better performance than selecion sort in terms of time.

We know that both mergesort(f) and heapsort(g)  have O(n logn) runing time.
In our "MergeSort vs. HeapSort" plot, two lines are parallel to each other most of the time.
This shows that f/g = constant, which means that the runing time of the two algorithms are different
by a constant factor.

------------------------------
Word Stemming and Punctuations
------------------------------
 For the punctuation part, we use the built in function "ispunct(c)" to check if 
the character is a punctuation or a character. If it is a punctuation, then 
just ignore (treat it like a space). However, due to the nature of 
the ispunct(c) function - it considers " ' " and " - " as
punctuations - there are chances for the side effects happen: "I'd" will be read as 2 
different words: "I" and "d", same as "he's" becomes "he" and "s". The other case can 
be "ice-cream" becomes "ice" and "cream". Therefore, we came to the decision of 
using one of our own functions--ispunctuation(c)--to eliminate the case 's and 'd, 
and '-'. This function will call ispunct(c) if c is not the ' and -. 

 For the word-stemming part, two stemming kinds are taken care: 
words end with -s and with -ly. Due to our language skill limitations,
we cannot check all the cases and all the exceptions. We have tried our best to check 
all of the cases that we think of. Also, since " 'd ", " 's " is in the scope above,
we remove them as well. For this option, one needs to add "-suf" in the command line as
mentioned above.

>>> print"=========="
==========
>>> my_file=open('C\Temp\sample.txt', 'r')

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    my_file=open('C\Temp\sample.txt', 'r')
IOError: [Errno 2] No such file or directory: 'C\\Temp\\sample.txt'
>>> import easygui
>>> easygui.msgbox('This is a basic message box.', 'Title goes Here')
'OK'
>>> import easygui
>>> user_response=easyqui.msgbox('This is a basic message box.', 'Title goes here')

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    user_response=easyqui.msgbox('This is a basic message box.', 'Title goes here')
NameError: name 'easyqui' is not defined
>>> user_response = easygui.msgbox('This is a basic message box.', 'Title Goes Here')
print user_response

>>> print user_response
OK
>>> import easygui
>>> easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
'Strawberry'
>>> print user_response
OK
>>> user_response = easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
>>> print user_response
Vanilla
>>> import easygui
>>> flavor = easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
>>> easygui.msgbox('You picked ' + flavor)
'OK'
>>> import easygui
>>> flavor = easygui.choicebox('Whatis is your favorite flavor.', choices = ['Chocolate', 'Vanilla', 'Strawberry'])
>>> easygui.msgbox('You picked ' + flavor)
'OK'
>>> import easygui
>>> flavor = easygui.choicebox('Whatis is your favorite flavor.', choices = ['Chocolate', 'Vanilla', 'Strawberry'])
>>> easygui.msgbox('You picked ' + flavor)

'OK'
>>> import easygui
>>> flavor = easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry','a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m'))
>>> easygui.msgbox('You picked ' + flavor)
'OK'
>>> import random, easygui
secret = random.randint(1,99)
>>> guess=0
>>> tries-0

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tries-0
NameError: name 'tries' is not defined
>>> import random, easygui
>>> secret = random.randint(1,99)
>>> guess = 0
>>> tries = 0
>>> easygui.msgbox("I have a secret! It is a number from 1 to 99.   I'll give you 6 tries")
'OK'
>>> while guess != secret and tries < 6:
	guess = easygui.integerbox("Please guess the number ~  (" + str(tries+1) + ")")
	if not guess: break
	if guess < secret:
		easygui.msgbox(str(guess) + " is too low, try again!")
	elif guess > secret:
		easygui.msgbox(str(guess) + " is too high, try more!")
	tries = tries + 1
if guess == secret:
	
SyntaxError: invalid syntax
>>> 
=============== RESTART: C:/Users/user/Desktop/NumGuessGame.py ===============
>>> 
