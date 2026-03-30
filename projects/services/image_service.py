from utils.compressor import check_image_size, optimize_image_to_webp


def process_project_image(image):
    if not image:
        return image

    check_image_size(image)

    if not image.name.lower().endswith(".webp"):
        return optimize_image_to_webp(image, quality=80)

    return image
