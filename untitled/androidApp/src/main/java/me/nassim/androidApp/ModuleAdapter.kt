package me.nassim.androidApp

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView


class ModuleAdapter(private val context: Context, private val list: ArrayList<President>): RecyclerView.Adapter<ModuleAdapter.ViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val moduleList = LayoutInflater.from(context).inflate(R.layout.item_module_vertical, parent, false)
        return ViewHolder(moduleList)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(list[position])
    }

    override fun getItemCount(): Int {
        return list.count()
    }

    inner class ViewHolder(itemView: View): RecyclerView.ViewHolder(itemView) {
        fun bind(item: President) {
            val productName = itemView.findViewById<TextView>(R.id.module_name)

            productName.text = item.name
        }

    }

}