import tempfile
import streamlit as st
from PIL import Image
from rembg import remove
import io


def remove_background(input_image):
    output_data = remove(input_image)

    return Image.open(io.BytesIO(output_data))


def main():
    st.title("Background Remover App")
    st.write("Upload an image, and the app will remove the background.")

    uploaded_file = st.file_uploader(
        "Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        if st.button("Remove Background"):
            st.spinner("Removing background...")
            try:
                path = ""
                # removed_background_image = remove_background(uploaded_file)
                removed_background_image = remove_background(
                    uploaded_file.getvalue())
                st.image(removed_background_image,
                         caption="Image with Background Removed", use_column_width=True)
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                st.spinner("")


if __name__ == "__main__":
    main()
