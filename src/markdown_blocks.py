def markdown_to_blocks(markdown):
    '''
    input: raw Markdown string (representing a full document)
    output: list of "block" strings
    '''
    # split the raw string into blocks based on double newlines
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        # remove leading/trailing whitespace 
        stripped_block = block.strip() 
        # only add to the list if the block is not empty 
        if stripped_block != "":
            filtered_blocks.append(stripped_block)

    return filtered_blocks