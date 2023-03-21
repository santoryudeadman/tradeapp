#!bin/bash
#configure compiler
js_dir="./"
js_files=(
    node_modules/axios/dist/axios.min.js
    node_modules/bootstrap/dist/js/bootstrap.bundle.js
    node_modules/venobox/dist/venobox.min.js
    src/app.js
)
css_dir="./"
css_files=(
    node_modules/bootstrap/dist/css/bootstrap.min.css
    node_modules/venobox/dist/venobox.min.css
    src/app.css
)

#Todo: autogenerate uploads directly
#updating modules
if [ -d "./node_modules" ]; then
#npm update
echo "done";
 else
npm install
fi
#cleaning build
rm -rf ./public/build
mkdir ./public/build
# Define the output directory and file names
output_dir="./public/build"
js_output_file="merged.min.js"
css_output_file="merged.min.css"
# Merge and minimize the JavaScript files
echo "Merging and minimizing JavaScript files..."
#cat "${js_files[@]/#/$js_dir/}" | npx uglifyjs --compress --mangle > "${output_dir}/${js_output_file}"
cat "${js_files[@]/#/$js_dir/}" > "${output_dir}/${js_output_file}"

# Merge and minimize the CSS files
echo "Merging and minimizing CSS files..."
#cat "${css_files[@]/#/$css_dir/}" | npx clean-css-cli --output "${output_dir}/${css_output_file}"
cat "${css_files[@]/#/$css_dir/}" > "${output_dir}/${css_output_file}"

echo "Merged and minimized files saved to ${output_dir}"