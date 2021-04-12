var grid = document.getElementsByClassName('grid')[0]

let $box_outer_to, $box_outer_from

const gridClickHandler = e => {
    new changeDirection(e).test("left").test("right").test("bottom").test("top")
}

class changeDirection{
    constructor(e){
        this.cell_data = parseInt(e.target.closest("td").dataset.cell);
        this.$cell = e.target.closest("td");
        this.row_data = parseInt(e.target.closest("tr").dataset.row);
        this.$row = e.target.closest("tr");
        $box_outer_from = this.$cell.children[0]
        this.$box = $box_outer_from.children[0];
    }

    test(direction){
        if (this.ok) return this;

        switch(direction){
            case "left":
                this.testLeft();
                break;
            case "right":
                this.testRight();
                break;
            case "top":
                this.testTop();
                break;
            case "bottom":
                this.testBottom();
                break;
        }
        return this;
    }

    testRight(){
        if(this.cell_data < 3){
            let $box_outer = this.$row.children[this.cell_data + 1].children[0]
            if(!$box_outer.children.length){
                $box_outer_to = $box_outer;
                this.ok = true
                grid.removeEventListener('click', gridClickHandler, false);
                this.$box.classList.add("move-right")
            }
        }
    }

    testLeft(){
        if(this.cell_data > 0){
            let $box_outer = this.$row.children[this.cell_data - 1].children[0]
            if(!$box_outer.children.length){
                $box_outer_to = $box_outer
                this.ok = true
                grid.removeEventListener('click', gridClickHandler, false);
                this.$box.classList.add("move-left")
            }
        }
    }

    testTop(){
        if(this.row_data > 0){
            let row_top_id = this.row_data - 1
            let $row_top = document.querySelector(`[data-row='${row_top_id}']`)
            let $box_outer = $row_top.children[this.cell_data].children[0]
            if(!$box_outer.children.length){
                $box_outer_to = $box_outer;
                this.ok = true
                grid.removeEventListener('click', gridClickHandler, false);
                this.$box.classList.add("move-top")
            }
        }
    }

    testBottom(){
        if(this.row_data < 3){
            let row_bottom_id = this.row_data + 1
            let $row_bottom = document.querySelector(`[data-row='${row_bottom_id}']`)
            let $box_outer = $row_bottom.children[this.cell_data].children[0]
            if(!$box_outer.children.length){
                $box_outer_to = $box_outer
                this.ok = true
                grid.removeEventListener('click', gridClickHandler, false);
                this.$box.classList.add("move-bottom")
            }
        }
    }
}

grid.addEventListener('click', gridClickHandler, false)

const transEndHandler = e => {
    swapBox(e.target.innerHTML);
    grid.addEventListener('click', gridClickHandler, false)
}

document.addEventListener("transitionend", transEndHandler, false)

const swapBox = num => {
    $box = document.createElement("div")
    $box.classList.add("box", "animate", "hidden")
    $box.innerHTML = num
    $box_outer_to.appendChild($box)
    $box_outer_from.children[0].remove()
    $box.classList.remove("hidden")
}
