mkdir package
cp -r lambdas package
cp -r dependencies/* package
cd package

find . -name "*.pyc" -exec rm -rf {} \;
find . -name "*.sw*" -exec rm -rf {} \;

zip -r lambdas.zip *
aws s3 cp lambdas.zip s3://mediasapiens-sources/bobik-lambdas.zip
aws lambda update-function-code --function-name Bobik --s3-bucket mediasapiens-sources --s3-key bobik-lambdas.zip

cd ..
rm -rf package
