IMAGE_PATH="./validation/hindi_tamil_ocr_eval_pdf_images2/*.jpg"
MODEL_PATH="./outputs/prima/mask_rcnn_R_50_FPN_3x/model_final.pth"
YAML_PATH="./outputs/prima/mask_rcnn_R_50_FPN_3x/config.yaml"
SAVE_PATH="./validation/hindi_tamil_ocr_eval_pdf_images2_result_post_process/"
CLASS_MAPPING={0:"MathRegion"}
RESUME=True
PRETRAINED_MODEL="./outputs/prima/mask_rcnn_R_50_FPN_3x/pre_trained_model.pth"
