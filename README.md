# VRT_data_extractor

# Description

Data extraction script is based on toolbox sport-activities-features. It uses toolbox classes to extract data from TCX file and calcualte needed variables for VRT_app

# Requirements

Python is required for data_extraction.py, avilable here: https://www.python.org/

For script to work we need to install sport-activities-features toolbox. 
Toolbox is available here: https://github.com/firefly-cpp/sport-activities-features


# Usage

1. Clone repository.

```
git clone https://github.com/mdezelak/VRT_data_extractor.git
```

2. Set proper sys.path inside `data_extraction.py` to where 'sport-activities-features' is installed.

```
sys.path.append('')
```

3. Set proper `path_to_file` inside `data_extraction.py` to where 'node.tcx' file is located in VRT_server folder.

```
activity  = tcx_file.read_one_file("path_to_file/node.tcx")
```
