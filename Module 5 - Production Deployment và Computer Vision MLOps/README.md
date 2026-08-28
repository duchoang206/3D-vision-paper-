# Module 5 - Production Deployment và Computer Vision MLOps

**Mục tiêu đầu ra:** Chuyển mô hình nghiên cứu thành dịch vụ hoặc pipeline video ổn định, đo được latency/throughput và quản lý vòng đời dữ liệu–mô hình.

## Danh sách phân mục
- [5.1 - Tối ưu mô hình và inference engine](./5.1 - Tối ưu mô hình và inference engine/README.md): PyTorch -> ONNX -> TensorRT, Post-Training Quantization (FP16/INT8), C++ Runtime (OpenCV + TensorRT), Benchmark Latency/FPS/VRAM.
- [5.2 - Pipeline video thời gian thực](./5.2 - Pipeline video thời gian thực/README.md): NVIDIA DeepStream SDK, GStreamer, HW Decode NVDEC/NVENC, Multi-stream RTSP, Queue/Jitter/Reconnect Management.
- [5.3 - MLOps cho Computer Vision](./5.3 - MLOps cho Computer Vision/README.md): Gán nhãn CVAT/Label Studio, DVC Data Versioning, MLflow/W&B Experiment Tracking, Triton Inference Server, Dockerization & Monitoring.
