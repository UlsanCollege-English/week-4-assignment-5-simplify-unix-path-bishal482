# src/simplify.py
from typing import List

def simplify_path(path: str) -> str:
    """
    Simplifies a Unix-style absolute path by resolving '.', '..', and multiple slashes.
    
    Args:
        path: The absolute path string (e.g., "/a/./b/../../c/").

    Returns:
        The canonical simplified path string (e.g., "/c").
    """
    
    # 1. Split the path by the slash '/' delimiter.
    # This automatically handles multiple consecutive slashes (e.g., "a///b" splits to ["a", "", "", "b"])
    segments: List[str] = path.split('/')
    
    # Use a stack to store the canonical directory names.
    stack: List[str] = []
    
    for segment in segments:
        # Ignore empty strings (from multiple slashes or leading/trailing slashes)
        # and ignore the current directory marker ('.').
        if segment == '' or segment == '.':
            continue
        
        # Handle the parent directory marker ('..').
        elif segment == '..':
            # If the stack is not empty, pop the last directory name (move up one level).
            # If the stack IS empty, we are at the root, and '..' is ignored 
            # (e.g., "/../../" -> stack remains empty).
            if stack:
                stack.pop()
        
        # Handle a valid directory name.
        else:
            stack.append(segment)

    # 2. Reconstruct the path from the stack.
    # The canonical path must always start with a single slash '/'.
    # Join the stack contents with a slash.
    
    if not stack:
        # If the stack is empty (e.g., path was "/", "/../", or "/./"), return the root.
        return "/"
    else:
        # Join the stack contents with '/' and prefix with a leading '/'.
        return "/" + "/".join(stack)