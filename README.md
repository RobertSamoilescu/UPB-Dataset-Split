# UPB-Dataset-Split

<p align="center">
  <img src="imgs/train_test_split.png" alt="train_test_split" width="512" />
</p>

## Create dataset 

```shell
mkdir raw_dataset
```

Copy the video recodings in the "raw_dataset" directory. A sample of the UPB dataset is available <a href="https://drive.google.com/drive/folders/1p_2-_Xo-Wd9MCnkYqPfGyKs2BnbeApqn?usp=sharing">here</a>.
Run the split_dataset notebook, but make sure to change the variable "path_jsons=./raw_dataset"
In the "img" directory you should get the geographical areas of the train, test/validation split and the combination of those. 
In the "split" directory you should get the scenes split for train and test/validation.
 
