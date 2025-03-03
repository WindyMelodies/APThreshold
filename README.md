# Action potential threshold dynamics analyzer (APThreshold)

## Overview
The action potential (AP) threshold controls spike initiation in single neurons and exhibits
considerable variability with recent firing history and input properties. Spike threshold dynamics enables neurons
to perform temporally precise coding. Quantifying and analyzing threshold dynamics usually requires multiple
ad-hoc programming, that is, obtaining APs, identifying threshold voltage, calculating spike features, and data
visualization. To facilitate analysis efficiency, we present the AP threshold dynamics analyzer (APThreshold),
which is a Python-based software tool with a user-friendly graphic user interface (GUI). We
implement the waveform curvature-based and ramp stimulation-based methods for threshold identification in
the software. The GUI is designed as an interactive tool, which enables users to visualize the data in a point-andclick manner and customize the coordinate axes of each plot without programming. This endows APThreshold
with the ability to examine the relationship between threshold voltage and spike features and analyze its
underlying biophysical basis. We provide three example workflows of how to use our software to
quantify the threshold dynamics in biophysical models or experimental recordings. The example results validate
the functionality and efficiency of the software in identifying spike threshold with the implemented methods.
Significance. APThreshold could be applied as an effective tool to analyze the threshold variability across cell
types.

## Features
- Simulate biophysical models
- Import experimental recordings
- Quantify and analyze spike threshold dynamics
- Visualize data in a point-and-click manner
- Graphical user interface (GUI)

## Installation
The software supports installation and execution across multiple operating systems (Windows, Linux, and
macOS). We provide two options to launch APThreshold: (1) Clone the [source code](https://github.com/WindyMelodies/APThreshold.git) and run it in a Python environment. (2)  Run the pre-built APThreshold.exe file for quick execution on Windows.
### Option 1: Running from Source Code (All Platforms)
We recommend using Anaconda to deploy the Python environment for APThreshold.
1. Install Anaconda and Git  
    Download Anaconda from https://www.anaconda.com/download/success.  
    Download Git from https://git-scm.com/downloads.  
2. Clone the APThreshold Repository    
    Open a terminal or command prompt and run:
    ```commandline
   git clone https://github.com/WindyMelodies/APThreshold.git
   ```
3. Set up conda environment  
    
    ```commandline
    conda env create --name APThreshold --file environment.yml
    conda activate APThreshold
    ```
4. Run APThreshold
    ```commandline
   cd APThreshold
   python main.py
   ```

### Option 2: Running as a Standalone .exe File (Windows Only)
1. Download the executable  
    [APThreshold.zip](https://github.com/WindyMelodies/APThreshold/releases/download/v1.0.0/APThreshold.zip)(contains the standalone version of APThreshold)
2. Extract the .zip file  
3. Run APThreshold  
    Click the 'APThreshold.exe' file.
    


> **Note:** The standalone version is currently available for Windows only.  
> For Linux and macOS users, please follow *Option 1: Running from Source Code*.

## Support

If you have issues, please contact us at guoshengyi@tju.edu.cn or pengzhanzhang@tju.edu.cn.

## Cite

If our software is helpful to your research, please cite the following reference in which we present APThreshold and demonstrate its ability with several use cases:
> ... Action potential threshold dynamics analyzer (APThreshold) ... todo
> 
## Author
Guosheng Yi, Pengzhan Zhang and Ruifeng Bai*  
School of Electrical and Information Engineering, Tianjin University, Tianjin, People’s Republic of China

## License

The project is licensed under the GPL-3.0 License.

