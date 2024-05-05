 #!/bin/bash

./do_cross_examination_transformer.sh
if [ $? -eq 0 ]; then
    echo "First script executed successfully."
    ./do_cross_examination_encoder_decoder.sh
else
    echo "First script failed. Exiting..."
fi
