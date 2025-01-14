https://whoisfawaz.hashnode.dev/mastering-real-time-performance-semaphore-benchmarking-and-latency-analysis-on-raspberry-pi-4-with-preemptrt

# 🚀 Semaphore Benchmarking and Latency Analysis on Raspberry Pi 4

## 📖 Overview

This repository features a comprehensive set of tools and scripts for benchmarking semaphore operations and analyzing system latency on a **Raspberry Pi 4 (RPi4)** using **cyclictest** under stress conditions with **PREEMPT_RT** (Real-Time Linux). Implemented in C and Python, this project provides deep insights into semaphore signaling, waiting times, and latencies in user space, kernel space, and IRQs.

## ✨ Features

- **Semaphore Benchmarking**: Measure the time taken for semaphore signaling and acquisition across multiple iterations on Raspberry Pi 4.
- **Latency Analysis**: Analyze and visualize latencies for user space, kernel space, and IRQs based on cyclictest outputs.
- **PREEMPT_RT Compatibility**: Optimized for real-time performance analysis on Raspberry Pi 4 with PREEMPT_RT patches.

## 📂 Repository Contents

- **`sem.c`**: C code for benchmarking semaphore signal and wait times using tasks with different priorities.
- **`sem_processing.c`**: C code for processing and benchmarking semaphore operations FOR Wait, Signal, Wait Block and Signal Unblock.
- **`cyclictestplotgraph.py`**: Python script for parsing and visualizing latency data from cyclictest outputs.

## 🚀 Getting Started

### 🛠️ Prerequisites

- **Raspberry Pi 4**: This project is specifically tailored for use on a Raspberry Pi 4 running a Linux distribution with PREEMPT_RT support.
- **C Compiler**: GCC or Clang for compiling the C benchmark programs.
- **Python 3.x**: Required for running the latency plotting script.
- **Matplotlib**: Python library for plotting data. Install it using pip:

    ```bash
    pip install matplotlib pandas
    ```

### 📥 Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/semaphore-benchmarking.git
    cd semaphore-benchmarking
    ```

2. **Compile the C Code**:

    ```bash
    gcc -o sem_benchmark sem.c -lpthread
    gcc -o sem_processing_benchmark sem_processing.c -lpthread
    ```

## 🏃 Usage

### 📊 Running Semaphore Benchmark

To execute the semaphore benchmarking tests on Raspberry Pi 4, run the compiled binaries:

```bash
./sem_benchmark
./sem_processing_benchmark
```
The results will be displayed in the console, showcasing the time taken for semaphore operations across multiple iterations.

### 📈 Analyzing Latency with cyclictest
Run cyclictest on the Raspberry Pi 4 with desired parameters and save the output to a file:
```bash
cyclictest -l100000 -m -n -S99 -p99 -q > cyclictest_output.txt
```

Use the provided Python script to parse and plot the data:
```bash
python cyclictestplotgraph.py
```
The script will display a graph showing latencies over time for user space, kernel space, and IRQs.

![image](https://github.com/user-attachments/assets/6573fdb3-48c7-42dc-b2b9-db0b4cb368f8)
![image](https://github.com/user-attachments/assets/2135888f-06aa-4326-992f-4eae9783528b)
![image](https://github.com/user-attachments/assets/f5470cc0-5126-41c9-9f58-df8ee2ed01f8)

