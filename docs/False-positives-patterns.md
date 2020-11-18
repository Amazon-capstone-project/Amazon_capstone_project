# Patterns of false positive cases

Keywords used in the first phase: "outdated", "out of date", "obsolete" and "deprecated".

## Observation from manually checked "false positives" comments

These comments contain the target keywords but are actually not indicating obsoleteness.

```tsv
	Id	PostId	UserId	outdated (manually checked)	answer outdated	question outdated
3	102530502.0	57812080.0		False		
17	103349458.0	58505922.0	2695716	False		
35	83478364.0	48247353.0	682485	False	0.0	0.0
37	83787006.0	48399493.0	699305	False	0.0	0.0
45	109988937.0	62175887.0	547733	True	0.0	1.0
55	99250604.0	56319766.0	1307905	True	0.0	1.0
111	110474963.0	62461548.0	4690946	False		
119	111738828.0	63172576.0	10931123	False		
122	106736985.0	60333506.0	1609570	False		
139	101646390.0	38313021.0	6248616	False	0.0	0.0
148	112642381.0	63699393.0	8822238	False	0.0	0.0
167	82631633.0	47818985.0	4278870	False	0.0	0.0
175	65330568.0	38986651.0	495796	False	0.0	0.0
179	111849266.0	63247775.0	13299635	False	0.0	0.0
241	95255983.0	23698987.0	1081275			
282	102530502.0	57812080.0	1017466			
387	111857562.0	63241324.0	1373856			
392	87411933.0	50194454.0	466862			
488	88896039.0	50948793.0	6624525			
627	38193785.0	21935218.0	2288548			
645	104397191.0	59071423.0	3858193			
712	42208996.0	26230395.0	3223711			
738	72295960.0	42572050.0	13070			
808	74603042.0	36339430.0	593036			
871	103349458.0	58505922.0	2695716			
```

They are matched by patterns including:

```text
 'outdated data',
 'data are outdated',
 'tags become old and outdated',
 'plugins installed that may be out of date',
 "I'm outdated",
 'non-obsolete',
 'flash is deprecated',
 'outdated disk',
 '`sensorId` gets obsolete',
 'obsolete actors',
 'not deprecated',
 'updateOutdatedInstancesOnly',
 'Browser was outdated',
 'not outdated'
```
