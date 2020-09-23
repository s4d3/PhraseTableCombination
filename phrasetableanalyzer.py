#!/usr/bin/python3
import sys

animation = "|/-\\"
ianim=0

phrasereport = []
VAL_PHRASE = lambda counter,x, y : 0 if x>y else 1 if x==y else 2

def print_animation():
  global ianim
  szbckspace="".join("\r" for i in range(len("Please Wait: |")))
  szanim = szbckspace + "Please Wait: "+animation[ianim % len(animation)]
  sys.stdout.write(szanim)
  ianim+=1


def print_keterangan(hfout):
  hfout.write("Keterangan: \n")
  hfout.write("    0 : value in file1 > value in file2 \n")
  hfout.write("    1 : value in file1 < value in file2 \n")
  hfout.write("    2 : value in file1 == value in file2 \n")


def countervalue(report,valuebase,value):
  if valuebase > value:
    report['0'] +=1
  elif valuebase < value:
    report['1'] +=1
  elif valuebase == value :
    report['2'] +=1


def phrasetable(fin1, fin2,foutput):
  hfout = open(foutput,'+w')
  hfin1 = open(fin1)
  hfin2 = open(fin2)
  lines = hfin1.readlines()
  lines2 = hfin2.readlines()
  
  for line in lines:
    phraseinfo = line.split('|||')
    valuebase = phraseinfo[2].split()
    report = {
      'phrase1':phraseinfo[0],
      'phrase2':phraseinfo[1],
      'scoreA1':valuebase[0],
      'scoreB1': valuebase[1],
      'scoreC1': valuebase[2],
      'scoreD1': valuebase[3],
      'valueA': {'0':0,'1':0,'2':0},
      'valueB': {'0':0,'1':0,'2':0},
      'valueC': {'0':0,'1':0,'2':0},
      'valueD': {'0':0,'1':0,'2':0},
    }
    
    for line2 in lines2:
      phraseinfo2 = line2.split('|||')
      if((phraseinfo[0] == phraseinfo2[0]) and (phraseinfo[1]==phraseinfo2[1]) ):
        values = phraseinfo2[2].split()
        countervalue(report['valueA'],float(valuebase[0]),float(values[0]))
        countervalue(report['valueB'],float(valuebase[1]),float(values[1]))
        countervalue(report['valueC'],float(valuebase[2]),float(values[2]))
        countervalue(report['valueD'],float(valuebase[3]),float(values[3]))
        if (any(elem['phrase1']==phraseinfo[0] and elem['phrase2'] == phraseinfo[1] and elem["scoreA1"] == valuebase[0] and
        elem["scoreB1"] == valuebase[1] and elem["scoreC1"] == valuebase[2] and elem["scoreD1"] == valuebase[3] 
        for elem in phrasereport)) == False :
          phrasereport.append(report)
      print_animation()
  print()
  print("Finished")
  hfout.write('Phrase Jp\tPhrase Id\tScore A1\tScore B1\tScore C1\tScore D1\tValue A – 00\tValue A – 01\tValue A – 02\tValue B – 00\tValue B – 01\tValue B – 02\tValue C – 00\tValue C – 01\tValue C – 02\tValue D – 00\tValue D – 01\tValue D – 02\n') 
  for info in phrasereport:
    hfout.write('%s\t%s\t%s\t%s\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n' %
        (
          info['phrase1'],info['phrase2'],
          info['scoreA1'],info['scoreB1'],info['scoreC1'],info['scoreD1'],
          info['valueA']['0'],info['valueA']['1'],info['valueA']['2'],
          info['valueB']['0'],info['valueB']['1'],info['valueA']['2'],
          info['valueC']['0'],info['valueC']['1'],info['valueC']['2'],
          info['valueD']['0'],info['valueD']['1'],info['valueD']['2'],
        )
      )
    hfout.flush()
  hfout.write("\n")
  hfout.write("\n")
  print_keterangan(hfout)


if __name__ == "__main__":
  phrasetable("phrase-table.Ru-En.LM03.gdfand-2000","phrase-table.Ru-En.LM03.srctotgt-12000","fileoutput-03.Ru-En.LM03.gdfand-srctotgt.12000.tsv")
