The Out the Window (OTW) dataset is a crowdsourced activity dataset containing 5,853 instances of 16 activities from the NIST Activities in Extended Video (ActEV) challenge.  These videos are crowdsourced from workers on the Amazon Mechanical Turk using a novel scenario acting strategy, which collects multiple instances of natural activities per scenario.  Turkers are instructed to lean their mobile device against an upper story window overlooking an outdoor space, walk outside to perform a scenario involving people, vehicles and objects, and finally upload the video to us for annotation.  Performance evaluation for activity classification on VIRAT Ground 2.0 shows that the OTW dataset provides an 8.3% improvement in mean classification accuracy, and a 12.5% improvement on the most challenging activities involving people with vehicles. 

## Visualization

<iframe width="560" height="315" src="https://www.youtube.com/embed/PB_FejlIlhc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Reference

If you use this dataset we ask that you cite:

G. Castanon, N. Shnidman, T. Anderson and J. Byrne, Out the Window: A Crowd-Sourced Dataset for Activity Classification in Surveillance Video, arXiv 2019


## OTW Dataset Description

This dataset features two parts - the Homes and Lots collections.  The Homes collection was created by workers on the Amazon Mechanical Turk, while the LOTS dataset was collected on-site at STR.

Annotation Instructions for the collected video can be found here:  

[https://docs.google.com/document/d/1Fks80zmtdc6CWL6CxKxQNB6BIoCeRynqBUFAzWRxUU0/edit?usp=sharing]

Note that this annotation document includes a total of 24 activities, but the dataset included here includes a total of 20 unique activities.

## Dataset statistics

```OTW-Homes:
Activity Type			Quantity
carrying (small)		372
closing trunk			293
unloading vehicle		332
mounting bike			70
loading vehicle			332
opening door			931
talking on phone		172
texting on phone		334
exiting			        334
dismounting bike		192
conversation			372
riding bike			166
entering			342
carrying (large)		307
pushing cart			90
opening trunk			289
closing door			925
```

```OTW-Lots:
Activity Type			Quantity
carrying (small)		8
closing door 			3
entering 			1
opening door			2
talking on phone		3
texting on phone		5
vehicle turning left    	137
vehicle turning right	        161
vehicle u-turn			1
```

## File structure

homes/videos/
lots/videos/

Videos containing activities of interest.  Unlike some activity datasets, these videos contain multiple activities of interest; annotations of these activities are provided in the accompanying annotation csvs.

homes/annotations.csv
lots/annotations.csv

## Annotation format

Annotation files are CSV format with schema:

[Video ID, Activity ID, Actor ID, Activity or Object Type, Frame Number, XMin, YMin, XMax, YMax, Labeled]

* Video ID: A globally unique ID assigned to each video for each dataset.   Each Homes video is located in homes/video/VIDEO_ID.mp4. Each Lots video is located in lots/video/VIDEO_ID.mp4

* Activity ID:
A unique ID assigned to each activity within a specific dataset (lots or homes).

* Actor ID: 
A unique ID assigned to each actor.  If we are not sure of the actor, this will be None.  

* Activity Type:
A label for the activity or object in the annotation

* Frame Number:
The frame number of the annotation.  Frame numbers correspond to the output of extract_frames.py

* XMin, YMin, XMax, YMax: 
The bounding box of the annotation defining the upper left corner (XMin, YMin) and bottom right corner (XMax, YMax) in image coordinates, where X=column index, Y=row index in image coordinates.

* Labeled: 
A boolean indicating whether or not a frame was Human Labeled (True) or Interpolated (False).  We used a combination of tracking and linear interpolation to generate bounding boxes in between the start and end frames of annotation by a human annotator.

Example annotations for a single activity from ./homes/annotations.csv:

```00000,0,00038,dismounting bike,252,82,1165,255,1586,True
00000,0,00038,person,252,85,1165,211,1446,True
00000,0,00038,bicycle,253,103,1230,250,1458,False
00000,0,00038,dismounting bike,253,85,1165,250,1458,False
00000,0,00038,person,253,85,1165,211,1446,False
00000,0,00038,bicycle,254,103,1229,254,1455,False
00000,0,00038,dismounting bike,254,85,1165,254,1455,False
00000,0,00038,person,254,85,1165,211,1446,False
00000,0,00038,bicycle,255,102,1226,255,1449,False
00000,0,00038,dismounting bike,255,85,1165,255,1449,False
00000,0,00038,person,255,85,1165,211,1446,False
```

Frames are 0-indexed.  Given an Activity Directory (homes|lots) and a Frame Number, the absolute path of an frame image filename is:

```img_file_name = os.path.join('.', 'homes', '%08d.jpg' % framenum)
```

## OTW to DIVA annotation

d_otw_to_diva.json is a JSON dictionary that maps OTW label string to their equivalent DIVA label string.  For example:

```OTW : DIVA
"carrying (large)":"transport_heavycarry",
"pushing cart":"pull"
```

## Frame extraction

A python3.x script for extracting frames from either the homes or lots datasets.

Usage:  

```pip3 install imageio imageio-ffmpeg
python3 extract_frames.py homes 
python3 extract_frames.py lots
```

This export will take a while, and will extract frames to ./homes/frames/*

The OTW-Lots dataset frame extraction requites 2.8TB.  Allocate drive space accordingly.

## License

Creative commons Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))

## Contact

Gregory Castanon  <<gregory.castanon@stresearch.com>>    
Jeffrey Byrne <<jeffrey.byrne@stresearch.com>>  

## Acknowledgement

Supported by the Intelligence Advanced Research Projects Activity (IARPA) via Department of Interior/ Interior Business Center (DOI/IBC) contract number D17PC00344. The U.S. Government is authorized to reproduce and distribute reprints for Governmental purposes notwithstanding any copyright annotation thereon. Disclaimer: The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies or endorsements, either expressed or implied, of IARPA, DOI/IBC, or the U.S. Government.
