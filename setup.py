from setuptools import setup, find_packages

setup(
    name='spark_tts',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'einops==0.8.0',
        'einx==0.3.0',
        'numpy==1.26.3',
        'pandas==2.2.3',
        'omegaconf==2.3.0',
        'packaging==23.2',
        'safetensors==0.4.5',
        'soundfile==0.12.1',
        'soxr==0.5.0.post1',
        'torch==2.2.0',
        'torchaudio==2.2.0',
        'tqdm==4.67.0',
        'transformers==4.46.2',
        'gradio==3.48.0',
    ],
    python_requires='>=3.12',
)