# Contributing Guidelines

## Getting Started
All translations are now submitted through our Weblate instance.

1. Make an account.
  - Go to https://weblate.lolc.at/accounts/register/
  - Follow the instructions.
2. Log in at https://weblate.lolc.at/accounts/login/
3. Translate!
  - Go to https://weblate.lolc.at/#suggestions
  - Choose a component.
  - Click on the `Translate` button for the component.

## Scripts
- Each component represents a single scene.
- Translated text should try to stick to 40 characters x 2 lines (80 characters total).

## CGs
  - CGs are currently not on Weblate. Please submit a PR for any changes.
  - Translate CGs & textures.
1. Edit them using image editor Photoshop/Gimp etc.
2. Open {cgs name}.json see the format.
3. Quantize colors using [PNGoo.exe](https://pngquant.org/).
4. -pspindex8 quantize to 256 color/-pspindex4 quantize to 16 color.
5. Saving & commiting the translated version( *.json, *.map, *.png)
  into the `cgs_translated` folder. 
  - Try to not change the palette of images when editing. 
  - Make sure to keep the alpha channel of textures (if there is one).
  - Don't forget to file an issue to let people know you are translating a piece of content!

