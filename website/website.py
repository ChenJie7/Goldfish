import gradio as gr

def addPDB(Path, Process):
    return f"{Process} for {Path} is registered "

demo = gr.Interface(    
    fn=addPDB, 
    inputs=[gr.Textbox(), gr.Radio(["Alphafold", "MPNN", "RFDiffusion", "Experiment"])], 
    outputs=gr.Textbox(),
    title="Goldfish Database",
    description="""<div style="display: flex; justify-content: center;">
                   <img src="https://raw.githubusercontent.com/ChenJie7/Goldfish/main/images/fish_protein.jpg" style="width: 400px; height: 300px; object-fit: cover;">
                   </div><br>
                   Tells us your pdb paths and the process which it was created and we will take care of the rest!""",
    allow_flagging="never"
)
demo.launch(share=True)
