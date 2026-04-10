import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, 
    QPushButton, QLabel, QTabWidget, QTextEdit
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize

class CiccioIVIMDKI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Ciccio IVIM DKI v2.0.0 - GE Healthcare')
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet("background-color: #f5f5f5;")
        
        # Central Widget
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🔬 Ciccio IVIM DKI v2.0.0")
        header_font = QFont()
        header_font.setPointSize(28)
        header_font.setBold(True)
        header.setFont(header_font)
        header.setStyleSheet("color: #1e88e5; padding: 20px;")
        layout.addWidget(header)
        
        # Subtitle
        subtitle = QLabel("Advanced MRI Analysis Framework - GE Healthcare")
        sub_font = QFont()
        sub_font.setPointSize(12)
        subtitle.setFont(sub_font)
        subtitle.setStyleSheet("color: #666; padding: 0px 20px 20px 20px;")
        layout.addWidget(subtitle)
        
        # Tabs
        tabs = QTabWidget()
        
        # Tab 1: Features
        features_widget = QWidget()
        features_layout = QVBoxLayout()
        features_text = QLabel("""
        ✅ IVIM Processing
           • Intravoxel Incoherent Motion analysis
           • Perfusion fraction estimation
           • Diffusion coefficient calculation
        
        ✅ DKI Analysis
           • Diffusional Kurtosis Imaging
           • Non-Gaussian diffusion assessment
           • Microstructural integrity metrics
        
        ✅ Clinical Diagnostics
           • Tumor characterization
           • Stroke detection
           • Neurodegeneration assessment
        
        ✅ 3D Visualization
           • Multi-planar reconstruction
           • 3D volume rendering
           • Interactive segmentation
        
        ✅ Machine Learning
           • Automated classification
           • Pattern recognition
           • Predictive analytics
        
        ✅ Report Generation
           • Clinical reports (PDF)
           • Data export (NIfTI, DICOM)
           • Quantitative metrics
        """)
        features_text.setStyleSheet("padding: 20px; font-size: 11px;")
        features_layout.addWidget(features_text)
        features_widget.setLayout(features_layout)
        tabs.addTab(features_widget, "Features")
        
        # Tab 2: About
        about_widget = QWidget()
        about_layout = QVBoxLayout()
        about_text = QLabel("""
        Ciccio IVIM DKI v2.0.0
        
        A comprehensive PyQt5-based framework for advanced MRI analysis
        developed in collaboration with GE Healthcare.
        
        🏥 Clinical Applications:
        • Oncology (tumor assessment)
        • Neurology (stroke, dementia)
        • Cardiology (myocardial fibrosis)
        
        🔧 Technical Stack:
        • Python 3.11 + PyQt5
        • NumPy, SciPy, scikit-learn
        • OpenCV, matplotlib, nibabel
        • Machine learning integration
        
        📊 Processing Capabilities:
        • Multi-shell DWI analysis
        • Quantitative parameter mapping
        • Statistical analysis
        • Batch processing
        
        Platform: Cross-platform (Windows, macOS, Linux)
        License: Medical Research Use Only
        Developer: Chameleon Labs
        """)
        about_text.setStyleSheet("padding: 20px; font-size: 10px; line-height: 1.6;")
        about_layout.addWidget(about_text)
        about_widget.setLayout(about_layout)
        tabs.addTab(about_widget, "About")
        
        layout.addWidget(tabs)
        
        # Buttons
        button_layout = QVBoxLayout()
        
        btn_start = QPushButton("▶️  Start Analysis")
        btn_start.setStyleSheet("""
            QPushButton {
                background-color: #1e88e5;
                color: white;
                padding: 12px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        button_layout.addWidget(btn_start)
        
        btn_settings = QPushButton("⚙️  Settings")
        btn_settings.setStyleSheet("""
            QPushButton {
                background-color: #424242;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 11px;
            }
        """)
        button_layout.addWidget(btn_settings)
        
        layout.addLayout(button_layout)
        
        # Footer
        footer = QLabel("v2.0.0 • GE Healthcare • © 2024 Chameleon Labs")
        footer.setStyleSheet("color: #999; padding: 15px; text-align: center; font-size: 9px;")
        layout.addWidget(footer)
        
        central.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CiccioIVIMDKI()
    sys.exit(app.exec_())
